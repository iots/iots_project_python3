
var xmlhttp;

function createXHR()
{
	//var xmlhttp = null;
	if(window.XMLHttpRequest){
		xmlhttp = new XMLHttpRequest();
	}else if(window.ActiveXObject){
		xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
	}else{
		xmlhttp = new ActiveXObject('Msxml2.XMLHTTP');
	}
	if(xmlhttp){
		;//alert('create xmlhttp success!');
	}else{
		alert('create xmlhttp error!');
	}
	//return xmlhttp;
}
window.onload=sendRequest()
function sendRequest()
{
	createXHR();
	var URL = "/work/query/";

	xmlhttp.open("GET",URL,true);
	xmlhttp.setRequestHeader("If-Modified-Since", "0");//清除缓存
	xmlhttp.onreadystatechange = on_button_query;  //response function.
	xmlhttp.send();
}


function on_button_query()
{
	if (xmlhttp.readyState == 4)
	{
	    if(xmlhttp.status == 200)
	    {
		//alert(xmlhttp.responseText);	
		//var txt = xmlhttp.responseText;
		var obj = JSON.parse(xmlhttp.responseText);  //JSON.parse() transform String into Object of JavaScript.
		online_info = 'Online Terminal: ' + obj.online;
		sent_info = 'Message Sent: ' + obj.sent;
		read_info = 'Message Read: ' + obj.read;
		document.getElementById('online_info').innerHTML=online_info;
		document.getElementById('sent_info').innerHTML=sent_info;
		document.getElementById('read_info').innerHTML=read_info;

		setTimeout("sendRequest()", 1000);
           }
	   else
	   {
		;//alert("error:" + xmlhttp.status);

	   }
	}
}


