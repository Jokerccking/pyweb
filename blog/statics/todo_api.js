var todoTemplate = function(todo){
	var t =	`
		<div class="todo-cell" data-id="${todo.id}">
			<div>${todo.content}</div>
			<time>"update time: ${todo.ut}"</time>
			<button class="todo-update">Update</button>
			<button class="todo-delete">Delete</button>
		</div>
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
		var form = {
			uid: ele.dataset.id,
			content: ele.querySelector(".content").value,
		};
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
			log("form:::",tdCell.dataset.id,form);
			var callBack = function(resp) {
				tdCell.remove();
			};

			ajax("POST","/todo/api/delete",form,callBack);
		}
	};
	bindClickEvent(ele,clickEvent);
};


var main = function() {
	todoAll();
	todoAdd();
	todoDelete();
};

main()
