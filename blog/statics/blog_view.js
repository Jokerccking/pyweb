var cmtTemplate = function(cmt) {
	var t = `
		<div class="cmt-cell" data-set="${ cmt.id}">
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
				<div><strong>Comments:</strong><div>
				<div class="cmtlist">

				</div>
				<form class="cmt-add" method="post" onsubmit="return checkForm()">
					<textarea class="cmt-content"></textarea>
					<button class="cmt-submit" type="submit">Comment</button>
				</form>
			</div><br>
		`;
};


var checkForm = function() {
}
