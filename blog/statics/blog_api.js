var cmtTemplate = function(cmt) {
	var t = `
			<div class="cmt-cell" data-id="${cmt.id}">
				<div class="cmt-content">${cmt.content}</div>
				Comment time: <time>${cmt.ct}</time>
				By: <user>${cmt.um}</user>
				<button class="cmt-delete">Delete</button>
			</div>
		`;
	return t;
}


var blogTemplate = function(blog) {
	var t = `
		<div id="id-blog-${blog.id}" class="blog-cell" data-id="${blog.id}">
			<div class="blog-content">${blog.content}</div>	
			Create time: <time>${blog.ct}</time>
			<button class="blog-delete">Delete</button>
			<div><strong>Comments:</strong></div>
			<div class="cmtlist">

			</div>
			<div class="cmtadd">
				<input class="cmtinput" type="textarea" palceholder="add comment"><br>
				<button class="cmtsubmit">Comment</button>
			</div>
		</div><br>
		`;
	return t;
};


var blogAll  = function() {
	var callBack = function(resp) {
		var bs = JSON.parse(resp);
		var bList = e("#id-blist");
		for (var i=0; i<bs.length; i++) {
			var bCell = blogTemplate(bs[i]);
			bList.insertAdjacentHTML("beforeend",bCell);
			var b = bList.querySelector("#id-blog-"+bs[i].id);
			var cmts = bs[i].comments;
			for (var j=0; j<cmts.length; j++) {
				cmtList = b.querySelector(".cmtlist");
				cmtCell = cmtTemplate(cmts[j]);
				cmtList.insertAdjacentHTML("beforeend",cmtCell);	
			}
		}
		log("Blogs load done");
	};

	ajax("GET","/blog/api/all","",callBack);
};


var blogAdd = function() {
	var ele = e("#id-badd");
	var clickEvent = function(event) {
		var targ = event.target;
		if (targ.classList.contains("badd")){
			var tt = ele.querySelector(".content");
			var form = {
				uid: ele.dataset.id,
				content: tt.value
			};
			tt.value = "";
			var callBack = function(resp) {
				log("add",JSON.parse(resp));
				var bCell = blogTemplate(JSON.parse(resp));
				var bList = e("#id-blist");
				bList.insertAdjacentHTML("beforeend",bCell);
			};
			ajax("POST","/blog/api/add",form,callBack);
		}
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

var cmtAdd = function() {
	var ele = e("#id-blist")
	var clickEvent = function(event) {
		var targ = event.target;
		if (targ.classList.contains("cmtsubmit")) {
			var bCell = targ.closest(".blog-cell");
			var cmtContent = bCell.querySelector(".cmtinput");
			var form = {
				bid: bCell.dataset.id,
				content: cmtContent.value,
			}
			cmtContent.value = "";
			var callBack = function(resp){
				var cmtCell = cmtTemplate(JSON.parse(resp));
				var cmtList = bCell.querySelector(".cmtlist");
				cmtList.insertAdjacentHTML("beforeend",cmtCell);
			};
			ajax("POST","/blog/api/cmtadd",form,callBack);
		}

	};
	bindClickEvent(ele,clickEvent);
};

var cmtDelete = function() {
	var ele = e("#id-blist");
	var clickEvent = function(event) {
		var targ = event.target;
		if (targ.classList.contains("cmt-delete")){
			var cmtCell = targ.parentElement; 
			var cmtId = cmtCell.dataset.id;
			var callBack = function(resp) {
				cmtCell.remove();
			};
			ajax("GET","/blog/api/cmtdel?id="+cmtId,"",callBack);
		}
	};
	bindClickEvent(ele,clickEvent);
};

var main = function() {
	blogAll();
	blogAdd();
	blogDelete();
	cmtAdd();
	cmtDelete();
};

main()
