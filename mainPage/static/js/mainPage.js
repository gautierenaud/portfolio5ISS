function initEverything() {
	addClickOnListHandler();
	retrieveContentList();
	retrieveContentInfo(9);
}

function retrieveContentList() {
	retrieveContent("contentInstance/getContentList", updateContentList);
}

function retrieveContentInfo(contentId) {
	retrieveContent("contentInstance/getContentInfo/" + contentId, updateContent);
}

function updateContentList(contentList) {
	$("#sidenav").html($("#sidenav").html() + contentList);
}

function updateContent(content) {
	$("#contentHolder").html(content);
}

function retrieveTagInfo(tagId) {
	retrieveContent("contentInstance/getArticleListFromTag/" + tagId, updateContent);
}

function retrieveContent(contentUrl, callbackFunc) {
	$.get(contentUrl, function( data ) {
		callbackFunc(data);
	});
}

function addClickOnListHandler() {
	$(document).on('click', '.nav li', function() {
		$(".nav li").removeClass("active");
		$(this).addClass("active");
	});
}

$(document).on("shown.bs.dropdown", ".dropdown", function () {
	// calculate the required sizes, spaces
	var $ul = $(this).children(".dropdown-menu");
	var $button = $(this).children(".dropdown-toggle");
	var ulOffset = $ul.offset();
	// how much space would be left on the top if the dropdown opened that direction
	var spaceUp = (ulOffset.top - $button.height() - $ul.height()) - $(window).scrollTop();
	// how much space is left at the bottom
	var spaceDown = $(window).scrollTop() + $(window).height() - (ulOffset.top + $ul.height());
	// switch to dropup only if there is no space at the bottom AND there is space at the top, or there isn't either but it would be still better fit
	if (spaceDown < 0 && (spaceUp >= 0 || spaceUp > spaceDown))
		$(this).addClass("dropup");
}).on("hidden.bs.dropdown", ".dropdown", function() {
	// always reset after close
	$(this).removeClass("dropup");
});
