import os
import urllib.parse
import argparse
from mitmproxy import proxy, options
from mitmproxy.tools.dump import DumpMaster
from mitmproxy import http


class WebCopy:
    def __init__(self, url, output):
        self.url = url
        self.host = urllib.parse.urlparse(url).hostname
        self.output = output

    def response(self, flow: http.HTTPFlow) -> None:
        if flow.request.pretty_host == self.host or flow.request.headers.get("Referer") == self.url:
            assert flow.response.status_code == 200
            if flow.request.path_components:
                file_path = os.path.join(self.output, *flow.request.path_components)
            else:
                file_path = os.path.join(self.output, "index.html")
            dirname = os.path.dirname(file_path)
            if not os.path.exists(dirname):
                os.makedirs(dirname)
            with open(file_path, "wb+") as f:
                f.write(flow.response.content)

def start(url, output):
    webcopy = WebCopy(url, output)
    opts = options.Options()
    pconf = proxy.config.ProxyConfig(opts)
    m = DumpMaster(opts)
    m.server = proxy.server.ProxyServer(pconf)
    m.addons.add(webcopy)

    try:
        m.run()
    except KeyboardInterrupt:
        m.shutdown()

def main():
    parser = argparse.ArgumentParser(description="网页复制工具")
    parser.add_argument("url", help="URL", type=str)
    parser.add_argument("-o", "--output", dest="output", help="输出文件位置", type=str, default='.')

    args = parser.parse_args()

    if not os.path.exists(args.output):
        os.makedirs(args.output)
    start(args.url, args.output)

if __name__ == '__main__':
    main()