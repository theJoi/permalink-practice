---
layout: module
title: TalkShow VS 4000 Form
joomla_module_id: 967
position: form
---
<!-- Module: TalkShow VS 4000 Form -->
<h2 style="text-align: center; font-size: 30px; margin-top: 0px; letter-spacing: 1px; font-family: 'HelveticaNeueThin', 'Helvetica Neue', Helvetica, Arial, sans-serif; font-weight: 100;">Speak with a<br /> Solutions Expert</h2>
<script src="/templates/newtekv2/js/marketoForms.js" type="text/javascript"></script>
<script src="//app-abq.marketo.com/js/forms2/js/forms2.min.js" type="text/javascript"></script>
<form id="mktoForm_2328"></form>
<div id="submit-msg" class="nm-modal">
	<h2>Thank You for connecting with NewTek!</h2>
	<p>A NewTek representative will contact you shortly.</p>
</div>
<script type="text/javascript">
	MktoForms2.loadForm("//app-abq.marketo.com", "900-QVC-131", 2328, function(form) {
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
<script type="text/javascript">
	Munchkin.createTrackingCookie();
	//Function to read value of a cookie
	function readCookie(name) {
		var cookiename = name + "=";
		var ca = document.cookie.split(';');
		for (var i = 0; i < ca.length; i++) {
			var c = ca[i];
			while (c.charAt(0) == ' ') c = c.substring(1, c.length);
			if (c.indexOf(cookiename) == 0) return c.substring(cookiename.length, c.length);
		}
		return null;
	}
	//Call readCookie function to get value of user's Marketo cookie
	var value = readCookie('_mkto_trk');
	encodeURIComponent(value);
</script>
<script type="text/javascript">
	MktoForms2.whenReady(function(form) {
		//set the first result as local variable
		var mktoLeadFields = mktoLead.result[0];
		//map your results from REST call to the corresponding field name on the form
		var prefillFields = {
			"Email": mktoLeadFields.email,
			"FirstName": mktoLeadFields.firstName,
			"LastName": mktoLeadFields.lastName,
			"Company": mktoLeadFields.company
		};
		//pass our prefillFields objects into the form.vals method to fill our fields
		form.vals(prefillFields);
	});
</script>
<link rel="stylesheet" href="/templates/newtekv2/css/modal.css" />
<script src="/templates/newtekv2/js/modal.js" type="text/javascript"></script>
