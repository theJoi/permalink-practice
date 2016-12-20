---
layout: module
title: 3Play Multi-Camera Editing Form
joomla_module_id: 1026
position: form
---
<style scoped="scoped" type="text/css">
	<!-- .channeltivity input, .channeltivity select, .channeltivity textarea {
		font-family: inherit;
		font-size: inherit;
		line-height: inherit;
		background: rgba(97, 97, 97, .55);
		color: #ccc !important;
		font-size: 16px;
		line-height: 40px !important;
		width: 100% !important;
		height: 42px;
		padding: 0px 20px;
		border: 1px solid rgba(255, 255, 255, .2);
		border-radius: 0;
		box-shadow: none !important;
	}
	.channeltivity {
		font-size: 16px;
		margin-top: 0px;
		letter-spacing: 1px;
		font-family:'HelveticaNeueThin', 'Helvetica Neue', Helvetica, Arial, sans-serif;
		font-weight: 100;
		padding-top:1em;
	}
	.channeltivity label {
		width:100%;
		margin-bottom: 2%;
	}
	-->
</style>
<!-- Module: Sports Video Form -->
<h2 style="text-align: center; font-size: 30px; margin-top: 0px; letter-spacing: 1px; font-family: 'HelveticaNeueThin', 'Helvetica Neue', Helvetica, Arial, sans-serif; font-weight: 100;">Speak with a Solutions Expert</h2>
<div class="channeltivity">
	<form method="POST" action="https://newtek.channeltivity.com/CTVT/ExternalFormImporter.aspx"><label>Company: <input name="Lead.Company" type="text" /></label><br /><label>First Name: <input name="Lead.FirstName" type="text" /></label><br /><label>Last Name: <input name="Lead.LastName" type="text" /></label><br /><label>Email: <input name="Lead.Email" type="text" /></label><br /><label>State/Province: <input name="Lead.StateProvince" type="text" /></label><br /><label>Country: <input name="Lead.Country" type="text" /></label><br /><label>Phone: <input name="Lead.Phone" type="text" /></label><br /><label style="display: none;">Lead Stage:<select name="Lead.LeadStage__c"><option value="310">Initial Call Made</option><option value="311">Second Call Made</option><option value="312">Interested</option><option value="313">Not Interested</option><option value="314">Needs Analysis</option><option value="315">Quote Provided</option><option value="316">Emailed</option><option value="317">Demo Requested</option></select></label><label>Additional Comments: <textarea name="Lead.AdditionalComments__c" cols="20" rows="10"></textarea></label><br /><br /><input name="Lead.Campaign" value="30" type="hidden" /><input name="Type" value="Lead" type="hidden" /><input name="RedirectUrl" value="http://www.newtek.com/3play/multi-cam-editing" type="hidden" /><input class="cta-blue cta-small align-center block" style="border: none; width: 100%; text-align: center; background-color: #0f99d6; text-transform: uppercase; font-size: 15px; letter-spacing: 2px; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-weight: 300; border-radius: 4px;" value="Submit" type="submit" />
	</form>
</div>
<!--<script src="/templates/newtekv2/js/marketoForms.js"> </script>
<script src="//app-abq.marketo.com/js/forms2/js/forms2.min.js"> </script>
<form id="mktoForm_2704"></form>
<div id="submit-msg" class="nm-modal">
	<h2>Thank You for connecting with NewTek!</h2>
	<p>A NewTek representative will contact you shortly.</p>
</div>
<script>
	MktoForms2.loadForm("//app-abq.marketo.com", "900-QVC-131", 2704, function(form) {
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
</script>-->
<link rel="stylesheet" href="/templates/newtekv2/css/modal.css" />
<script src="/templates/newtekv2/js/modal.js" type="text/javascript"></script>
