# Upload via API

以下是通过 API 上传文件的示例代码。假设 API 的基础 URL 为 `http://localhost:8080/`。

```javascript
let axios = require("axios").default;
let FormData = require('form-data');
let fs = require('fs');

// 配置项
//const project_id = '<项目标识符>';
const table_id = '<表标识符>';
const xc_token = '<授权令牌>';
const file_path = '<本地文件路径>';

// 上传图片
// @param image_path : 本地文件路径
// @return : 用于附件字段在插入记录 API 中的 JSON 对象
async function insertImage(path) {
    const formData = new FormData();
    formData.append("file", fs.createReadStream(path));
    const data = await axios({
        url: 'http://localhost:8080/api/v2/storage/upload',
        data: formData,
        headers: {
            'Content-Type': `multipart/form-data;`,
            'xc-token': xc_token
        },
        method: 'post',
        // 可选：存储文件路径
        params: { "path": "somePath" }
    });
    return data;
}

// 插入带有附件的记录
// 假设表包含两个列：
//      'Title' 类型为 SingleLineText
//      'Attachment' 类型为 Attachment
async function uploadFileExample() {
    let response = await insertImage(file_path);
    let row = {
        "Title": "2",
        "Attachment": response.data
    };
    await axios({
        method: 'POST',
        url: `http://localhost:8080/api/v2/tables/${table_id}/records`,
        data: row,
        headers: {
            'xc-token': xc_token
        }
    });
}

(async () => {
    await uploadFileExample();
})();
```

---

```javascript
let axios = require("axios").default;
let FormData = require('form-data');
let fs = require('fs');

// 配置项
//const project_id = '<项目标识符>';
const table_id = '<表标识符>';
const xc_token = '<授权令牌>';

// URL 数组：要上传的文件 URL 列表
const URLs = [{ url: '<URL1>' }, { url: '<URL2>' }];

// 通过 URL 上传图片
// @param URLs : 包含要上传文件的公共 URL 的数组
// @return : 用于附件字段在插入记录 API 中的 JSON 对象
async function insertImageByURL(URL_array) {
    const data = await axios({
        url: 'http://localhost:8080/api/v2/storage/upload-by-url',
        data: URL_array,
        headers: {
            'xc-token': xc_token
        },
        method: 'post',
        // 可选：存储文件路径
        params: { "path": "somePath" }
    });
    return data;
}

// 插入带有附件的记录
// 假设表包含两个列：
//      'Title' 类型为 SingleLineText
//      'Attachment' 类型为 Attachment
async function uploadByUrlExample() {
    let response = await insertImageByURL(URLs);
    // 更新两个列：Title 和 Attachment
    let row = {
        "Title": "3",
        "Attachment": response.data
    };
    await axios({
        method: 'POST',
        url: `http://localhost:8080/api/v2/tables/${table_id}/records`,
        data: row,
        headers: {
            'xc-token': xc_token
        }
    });
}

(async () => {
    await uploadByUrlExample();
})();
```