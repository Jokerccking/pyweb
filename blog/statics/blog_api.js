var blogTemplate = function(blog) {
	var t = `
		<div class="blog-cell" data-id="${blog.id}">
			<div class="blog-content">${blog.content}</div>	
			Update time: <time>${blog.ut}</time>
			<button class="blog-delete">Delete</button>
			<div><strong>Comments:</strong></div>
			<div id="id-cmtlist">

			</div>
			<div class="cmtadd">
				<input class="cmtinput" type="textarea"><br>
				<button class="cmtsubmit">Comment</button>
			</div>
		</div><br>
		`;
	return t;
};


var blogAll  = function() {
	var callBack = function(resp) {
		var bs = JSON.parse(resp);
		for (var i=0; i<bs.length; i++) {
			var bCell = blogTemplate(bs[i]);
			var bList = e("#id-blist");
			bList.insertAdjacentHTML("beforeend",bCell);
		}
		log("Blogs load done");
	};

	ajax("GET","/blog/api/all","",callBack);
};


var blogAdd = function() {
	var ele = e("#id-badd");
	var clickEvent = function() {
		var form = {
			uid: ele.dataset.id,
			content: ele.querySelector(".content").value
		};
		var callBack = function(resp) {
			var bCell = blogTemplate(JSON.parse(resp));
			var bList = e("#id-blist");
			bList.insertAdjacentHTML("beforeend",bCell);
		};
		ajax("POST","/blog/api/add",form,callBack);
	};

	bindClickEvent(ele, clickEvent);
};

var blogDelete = function() {
	var ele = e("#id-blist");
	var clickEvent = function(event) {
		var targ = event.target;
		if (targ.classList.contains("blog-delete")) {
			var bCell = targ.parentElement;
			var bid = bCell.dataset.id;
			var callBack = function(resp) {
				bCell.remove();
			};
			ajax("GET","/blog/api/delete?id="+bid,"",callBack);
		}
	};

	bindClickEvent(ele,clickEvent);
};








var cmtTemplate = function(cmt) {
	var t = `
			<div class="cmt-cell" data-id="${cmt.id}">
				<div class="cmt-content">${cmt.content}</div>
				Comment time: <time>${cmt.ct}</time>
				<button class="cmt-delete">Delete</button>
			</div>
		`;
}

var cmtAll = function() {
	var ele = e(
	var callBack = function() {

	};
	ajax("GET","/cmt/api/all","",callBack)
};


var main = function() {
	blogAll();
	blogAdd();
	blogDelete();
};

main()
