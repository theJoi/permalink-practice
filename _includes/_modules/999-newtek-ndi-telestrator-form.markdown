---
layout: module
title: NewTek NDI Telestrator Form
joomla_module_id: 999
position: form
---
<!-- Module: Telestrator Form -->
<h2 style="text-align: center; font-size: 34px; line-height: 40px; margin-top: 0px; letter-spacing: 1px; font-family: 'HelveticaNeueThin', 'Helvetica Neue', Helvetica, Arial, sans-serif; font-weight: 100;">Download the Demo</h2>
<p style="padding: 0px 5% 0px 5%;">Try a watermarked version of NewTek NDI Telestrator in your workflow for free.</p>
<script src="/templates/newtekv2/js/marketoForms.js" type="text/javascript"></script>
<script src="//app-abq.marketo.com/js/forms2/js/forms2.min.js" type="text/javascript"></script>
<form id="mktoForm_2352" target="_blank"></form>
<div id="submit-msg" class="nm-modal">
	<h2>Thank You for connecting with NewTek!</h2>
	<p>Thank you for your interest in the free NewTek NDI Telestrator Demo production application. You may download the production application by clicking the link below.</p>
	<p class="cta-container"><a href="http://new.tk/NDITelestrator" target="_blank" class="cta-blue cta-small align-center block">Download</a>
	</p>
	<p style="padding-top: 1em; padding-bottom: 2em;">Please be aware that NewTek NDI Telestrator Demo includes on-screen watermark on video output. For a version of the application without a watermark, please visit the <a href="https://store.newtek.com/index.php/ip/telestrator.html" target="_blank">NewTek Store</a>.</p>
</div>
<script type="text/javascript">
	MktoForms2.loadForm("//app-abq.marketo.com", "900-QVC-131", 2352, function(form) {
		NEWTEKV2.marketoForms.overlay_labels();
		MktoForms2.onFormRender(function() {
			NEWTEKV2.equal_heights();
		});
		form.onSuccess(function() {
			document.querySelector('button.mktoButton').innerHTML = 'Thank You';
			NEWTEKV2.modal.show('submit-msg');
			return false;
		});
	});
</script>
<link rel="stylesheet" href="/templates/newtekv2/css/modal.css" />
<script src="/templates/newtekv2/js/modal.js" type="text/javascript"></script>
