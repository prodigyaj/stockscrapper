var webPage = require('webpage');
var system = require('system');
var page = webPage.create();
page.settings.resourceTimeout = 5000; // 5 seconds
var url = system.args[1];

page.open(url, function (status) {
        if(status === 'success') {
        var content = page.content;
        console.log(content);
        phantom.exit();
        }
        else
        {console.log("Error!")
        phantom.exit()
        }
        });
