from pathlib import Path
import scrapy

class EtymonlineSpider(scrapy.Spider):
    name = "etymonline"

    def start_requests(self):
        # 生成 page, q 和 type 的组合
        for page in range(1, 8):  # page 从 1 到 7
            for q in range(ord('a'), ord('z') + 1):  # q 从 'a' 到 'z'
                for type_ in range(3, 6):  # type 从 3 到 5
                    url = f"https://www.etymonline.com/search?page={page}&q={chr(q)}&type={type_}"
                    yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # 提取 page, q, type 参数
        page = response.url.split("page=")[1].split("&")[0]
        q = response.url.split("q=")[1].split("&")[0]
        type_ = response.url.split("type=")[1].split("&")[0]

        # 使用 page, q, type 来动态生成文件名
        filename = f"etymonline-page{page}-q{q}-type{type_}.html"
        
        # 保存文件
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
