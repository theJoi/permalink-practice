---
layout: module
title: Advanced IP Workflow Video Gallery
joomla_module_id: 804
position: gallery
---
<!-- module: IP Workflow Video Gallery -->
<style scoped="scoped" type="text/css">
	<!-- .gallery-container .content-container {
		background-color: #f0f0f0;
		padding: 0 80px 15px;
	}
	.gallery-container h2 {
		font-family:'Helvetica Neue', Helvetica, Arial, sans-serif;
		color: #4f4e4e;
		text-align: center;
		font-size: 5rem;
		line-height: 5rem;
		font-weight: 200;
		padding: 0;
		margin: 60px 0 45px;
		letter-spacing: 0;
	}
	.gallery-container .gallery {
		margin-bottom: 60px;
	}
	.gallery-container .gallery .gallery-selected {
		margin-bottom: 10px;
	}
	.gallery-container .gallery .gallery-selected iframe {
		border-radius: 10px;
		box-shadow: 2px 4px 19px 1px rgba(0, 0, 0, .15);
		max-height: 657px;
	}
	.gallery-container .gallery .gallery-list {
		list-style: none;
	}
	.gallery-container .gallery .gallery-list a {
		display: block;
		text-decoration: none;
		color: #222;
		background: #fff;
		transition: background .2s;
		border-radius: 4px;
		overflow: hidden;
		border: 1px solid #ddd;
	}
	.gallery-container .gallery .gallery-list a:hover, .gallery-container .gallery .gallery-list a:focus {
		color: #428bca
	}
	.gallery-container .gallery .gallery-list a.active {
		color: #0074b1;
	}
	.gallery-container .gallery .gallery-list a .video-thumb {
		width: 100%;
		opacity: .75;
		transition: opacity .2s;
	}
	.gallery-container .gallery .gallery-list a .content {
		padding: 10px 15px;
	}
	.gallery-container .gallery .gallery-list a.active .video-thumb, .gallery-container .gallery .gallery-list a:hover .video-thumb {
		opacity: 1;
	}
	.gallery-container .gallery .gallery-list a .video-title {
		font-size: 2rem;
		margin-bottom: 0;
	}
	.gallery-container .gallery .gallery-list a .video-description {
		width: auto;
		text-align: left;
	}
	@media(max-width: 991px) {
		.gallery-container .gallery .gallery-list a .video-description {
			display: none;
		}
	}
	@media(max-width: 768px) {
		.gallery-container .content-container {
			padding: 0 20px 15px;
		}
		.gallery-container .gallery-list li {
			width: 24.25%;
			margin-left: 1%;
		}
		.gallery-container .gallery-list li:first-child {
			margin-left: 0;
		}
	}
	@media(max-width: 640px) {
		.gallery-container .gallery .gallery-selected {
			margin-bottom: 0;
		}
		.gallery-container .gallery .gallery-list a {
			line-height: 44px;
			background: #ccc;
			border: none;
		}
		.gallery-container .gallery .gallery-list a.active {
			background: #009add;
		}
		.gallery-container .gallery .gallery-list a .video-thumb {
			display: none;
		}
		.gallery-container .gallery .gallery-list a .content {
			padding: 0;
		}
		.gallery-container .gallery .gallery-list a .video-title {
			text-align: center;
		}
		.gallery-container .gallery .gallery-list a.active .video-title {
			color: #fff;
		}
	}
	-->
</style>
<div class="content-container padding-bleed clearfix">
	<h2>Decoding the Advanced IP Workflow</h2>
	<div id="ip-video-gallery" class="gallery clearfix">
		<div class="gallery-selected"><iframe id="selected-video" src="https://player.vimeo.com/video/137849706" width="100%" height="657px" frameborder="0" webkitallowfullscreen="" mozallowfullscreen="" allowfullscreen="allowfullscreen"></iframe>
		</div>
		<ul class="gallery-list clearfix">
			<li class="span3"><a href="javascript:;" class="gallery-thumb active" data-src="https://player.vimeo.com/video/137849706"> <img class="video-thumb" alt=" " title="" src="{{"images/gallery-thumb-ip-workflow-video-1.jpg" | cdn }}" />
<div class="content">
<p class="video-title">Part 1</p>
<p class="video-description">The Transition to IP</p>
</div>
</a>
			</li>
			<li class="span3 col"><a href="javascript:;" class="gallery-thumb" data-src="https://player.vimeo.com/video/137849747"> <img class="video-thumb" alt=" " title="" src="{{"images/gallery-thumb-ip-workflow-video-2.jpg" | cdn }}" />
<div class="content">
<p class="video-title">Part 2</p>
<p class="video-description">NewTek's Advanced IP Workflow</p>
</div>
</a>
			</li>
			<li class="span3 col"><a href="javascript:;" class="gallery-thumb" data-src="https://player.vimeo.com/video/137849761"> <img class="video-thumb" alt=" " title="" src="{{"images/gallery-thumb-ip-workflow-video-3.jpg" | cdn }}" />
<div class="content">
<p class="video-title">Part 3</p>
<p class="video-description">Advanced IP Workflow and TriCaster</p>
</div>
</a>
			</li>
			<li class="span3 col"><a href="javascript:;" class="gallery-thumb" data-src="https://player.vimeo.com/video/137849769"> <img class="video-thumb" alt=" " title="" src="{{"images/gallery-thumb-ip-workflow-video-4.jpg" | cdn }}" />
<div class="content">
<p class="video-title">Part 4</p>
<p class="video-description">Advanced IP for Everyone</p>
</div>
</a>
			</li>
		</ul>
	</div>
	<script src="templates/newtekv2/js/custom/ip-workflow.js" type="text/javascript"></script>
	<script type="text/javascript">
		NEWTEKV2.scale_video('selected-video', .65);
		NEWTEKV2.equal_heights(document.querySelectorAll('.gallery-list .content'));
	</script>
</div>
