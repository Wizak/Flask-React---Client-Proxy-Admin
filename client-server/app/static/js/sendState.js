function makeid(length) {
    var result = '';
    var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var charactersLength = characters.length;
    for ( var i = 0; i < length; i++ ) {
        result += characters.charAt(Math.floor(Math.random() * 
    charactersLength));
    }
    return result;
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

function setCookie() {
    var is_exist = document.cookie.indexOf('end_user_id=');
    if (is_exist == -1) {
        var id = makeid(20);
        document.cookie = 'end_user_id=' + id;
    }  
}

function RespData(data) {
    fetch("http://127.0.0.1:6001/api/v1/receiver?token=Q6A3hpmZt7", {
        method: 'POST', 
        headers: {
            'Content-type': 'application/json',
            'Accept': 'application/json'
        },
        body:JSON.stringify(data)
    }).then(res => {
        if (res.ok) {
            return res.json()
        } else {
            console.log('Client ERROR')
        }
    }).then(jsonResponse => {
        console.log(jsonResponse)
    }).catch((err) => console.error(err));
}

function Receive() {
    setCookie()
    const data = {
        'end_user_id': ''+getCookie('end_user_id'),
        'web_page_url': ''+window.location.pathname
    }
    RespData(data)
}

window.onload = Receive;