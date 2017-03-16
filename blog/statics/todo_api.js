var todoTemplate = function(todo){
	var t =	`
		<div class="todo-cell" data-id="${todo.id}">
			<div class="todo-content">${todo.content}</div>
			Update time: <time> ${todo.ut}</time>
			<button class="todo-delete">Delete</button><br>
			<input class="todo-input">
			<button class="todo-update">Update</button>
		</div>
		<br>
		`;	
	return t;
}	

var todoAll = function() {
	var callBack = function(resp){
		var tds = JSON.parse(resp);

		for (var i=0; i<tds.length; i++) {
		  var tdCell = todoTemplate(tds[i]);
			var tdList = e("#id-tdlist");
			tdList.insertAdjacentHTML("beforeend",tdCell);
		}
		log("todos load done");
	};

	ajax("GET","/todo/api/all","",callBack);
};


var todoAdd = function() {
	var ele = e("#id-tdadd");

	var clickEvent = function() {
		var tt = ele.querySelector(".content");
		var form = {
			uid: ele.dataset.id,
			content: tt.value
		};
		tt.value = "";
		var callBack = function(resp) {
			var tdList = e("#id-tdlist");
			var tdCell = todoTemplate(JSON.parse(resp));
			tdList.insertAdjacentHTML("beforeend",tdCell);
		};
		ajax("POST","/todo/api/add",form,callBack);
	};

	bindClickEvent(ele.querySelector(".tdadd"),clickEvent);
};


var todoDelete = function() {
	var ele = e("#id-tdlist");
	var clickEvent = function(event) {
		var targ = event.target;
		if (targ.classList.contains("todo-delete")){
			var tdCell = targ.parentElement;
			var form = { 
				id: tdCell.dataset.id
			};
			var callBack = function(resp) {
				tdCell.remove();
			};

			ajax("POST","/todo/api/delete",form,callBack);
		}
	};
	bindClickEvent(ele,clickEvent);
};


var todoUpdate = function() {
	var ele = e("#id-tdlist");
	var clickEvent = function(event) {
		var tar = event.target;
		if (tar.classList.contains("todo-update")) {
			var tdCell = tar.parentElement;
			var form = {
				tid: tdCell.dataset.id,
				content: tdCell.querySelector("input").value
			};
			var callBack = function(resp) {
				var td = JSON.parse(resp);
				tdCell.querySelector(".todo-content").innerHTML = td.content;
				tdCell.querySelector("time").innerHTML = td.ut;
			};
		
			ajax("POST","/todo/api/update",form,callBack);
		}
	};
	bindClickEvent(ele, clickEvent);
}

var main = function() {
	todoAll();
	todoAdd();
	todoDelete();
	todoUpdate();
};

main()
