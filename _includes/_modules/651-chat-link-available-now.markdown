---
layout: module
title: Chat Link (Available Now)
joomla_module_id: 651
position: chat-link
---
<script type="text/javascript">// <![CDATA[
/* free code from dyn-web.com */
function getDocHeight(doc) {
    doc = doc || document;
    // from http://stackoverflow.com/questions/1145850/get-height-of-entire-document-with-javascript
    var body = doc.body, html = doc.documentElement;
    var height = Math.max( body.scrollHeight, body.offsetHeight, 
        html.clientHeight, html.scrollHeight, html.offsetHeight );
    return height;
}
function setIframeHeight(id) {
    var ifrm = document.getElementById(id);
    var doc = ifrm.contentDocument? ifrm.contentDocument: ifrm.contentWindow.document;
    ifrm.style.visibility = 'hidden';
    ifrm.style.height = "10px"; // reset to minimal height in case going from longer to shorter doc
    // some IE versions need a bit added or scrollbar appears
    ifrm.style.height = getDocHeight( doc ) + 4 + "px";
    ifrm.style.visibility = 'visible';
}
// ]]></script>
<iframe id="ifrm" name="ifrm" src="siteIncludes/chat-link.php" onload="setIframeHeight(this.id)" style="width: 100%;" width="100%"></iframe>
