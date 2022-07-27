import io from 'socket.io-client';

const socket = io.connect("http://127.0.0.1:6001");

export default (action, collection, payload = {})=> 
new Promise((resolve, reject)=> {
    socket.emit('remote-call', {action, collection, payload}, (response)=>{
        if(response.error){
            console.log(response);
            reject(response);	
        }else{
            console.log(response);
            resolve(response);
        }
    }) 
    // socket.on("receive_message", msg => {
    //     if(msg.error){
    //         reject(msg);
    //     }else{
    //         console.log(msg)
    //         resolve({data:[{id:1,src:'a.jpg'}, {id:2,src:'b.jpg'}],total:2});
    //     }
    // });
    // socket.emit('remote-call', (response)=>{
    //     if(response.error){
    //         console.log(JSON.stringify(response))
    //         reject(response);	
    //     }else{
    //         console.log(JSON.stringify(response))
    //         //resolve({data:[{id:1,src:'a.jpg'}],total:1});	
    //         resolve(response);
    //     }
    // }) 
})
