function displayFullName() {
            // 创建 XMLHttpRequest 对象
            var request = new XMLHttpRequest();
            // debugger
            // 实例化请求对象
            request.open("GET", "https://c.biancheng.net/");
            // 监听 readyState 的变化
            request.onreadystatechange = function () {
                // 检查请求是否成功
                if(this.readyState === 4 && this.status === 0) {
                    // 将来自服务器的响应插入当前页面
                    // document.getElementById("result").innerHTML = this.readyState;
                }
            };
            // 将请求发送到服务器
            request.send();
        }
        // displayFullName()


