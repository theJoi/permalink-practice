---
layout: module
title: Hide Page from Production
joomla_module_id: 899
position: hide-prod
---
{source}<span style="font-family: courier new, courier, monospace;"><br /><span>&lt;</span>?php<br /><img src="/media/sourcerer/images/tab.png" | cdn }}" alt="&nbsp;&nbsp;&nbsp;&nbsp;" />if (strpos($_SERVER['HTTP_HOST'], 'www.newtek.com') !== false) {<br /><img src="/media/sourcerer/images/tab.png" | cdn }}" alt="&nbsp;&nbsp;&nbsp;&nbsp;" /><img src="/media/sourcerer/images/tab.png" | cdn }}" alt="&nbsp;&nbsp;&nbsp;&nbsp;" />header('Location: http://www.newtek.com', true, 302);<br /><img src="/media/sourcerer/images/tab.png" | cdn }}" alt="&nbsp;&nbsp;&nbsp;&nbsp;" /><img src="/media/sourcerer/images/tab.png" | cdn }}" alt="&nbsp;&nbsp;&nbsp;&nbsp;" />exit;<br /><img src="/media/sourcerer/images/tab.png" | cdn }}" alt="&nbsp;&nbsp;&nbsp;&nbsp;" />}<br />?<span>&gt;</span><br /></span>{/source}
