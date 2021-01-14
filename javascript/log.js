new Vue({
    el: ".show",
    data:{
        logs:[
            {
                date:"2020-12-31",
                txt:["解决了发送请求后返回的文本出现编码异常的问题"],
                say:"新年快到了,预祝大家新年快乐，本次更新了【windows 32位 0.1.1】版本，64位系统也将随即推出最新版本。",
                version:"0.1.1",
                filepath:"downloads/v0.1.1.html"
            },
            {
                date:"2021-1-12",
                txt:["优化了一些细节问题", "支持对表单的显示"],
                say:"您会注意到这次更新使界面焕然一新。",
                version: "0.1.2",
                filepath:"downloads/v0.1.2.html"
            }
        ]
    }
})