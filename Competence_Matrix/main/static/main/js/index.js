function tree_toggle(event) {
	event = event || window.event
	var clickedElem = event.target || event.srcElement
	if (!hasClass(clickedElem, 'Expand')) {
		return
	}
	var node = clickedElem.parentNode
	if (hasClass(node, 'ExpandLeaf')) {
		return
	}
	var newClass = hasClass(node, 'ExpandOpen') ? 'ExpandClosed' : 'ExpandOpen'
	var re =  /(^|\s)(ExpandOpen|ExpandClosed)(\s|$)/
	node.className = node.className.replace(re, '$1'+newClass+'$3')
}
function hasClass(elem, className) {
	return new RegExp("(^|\\s)"+className+"(\\s|$)").test(elem.className)
}
function UpdateCookieModel(modelName, modelType){
	document.cookie = "model"+modelType+"=" + modelName;
	document.cookie = "currentModelType="+modelType;
}
function ChangeModalWindow(modelType){
	let array = document.cookie.split(';');
	for(let i = 0; i < array.length; i++){
		let char = array[i];
		while(char.charAt(0) == ' '){
			char = char.substring(1);
		}
		if(char.indexOf("model"+modelType+"=") == 0){
			document.getElementById("modelName_Change").innerHTML = char.slice(("model"+modelType+"=").length);
		}
		else{
			document.getElementById("modelName_Change").innerHTML = "";
		}
	}
}
function AddModalWindow(modelType){
	document.cookie = "currentModelType="+modelType;
}
function SaveModelInfo(){
	document.cookie = "modelName="+ document.getElementById("modelName_Change").innerHTML;
	document.cookie = "modelDescription="+document.getElementById("modelDescription_Change").value;
	document.cookie = "modelNameAdd="+ document.getElementById("modelName_Add").value;
	document.cookie = "modelDescriptionAdd="+document.getElementById("modelDescription_Add").value;
}