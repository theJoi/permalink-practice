---
layout: module
title: LWE1110 Lead Form
joomla_module_id: 100
position: LWE1110-sugarform
---
<script src="/includes/js/regionCountryState.js" type="text/javascript">// <![CDATA[
&nbsp;
// ]]></script>
<script type="text/javascript">// <![CDATA[
function ClearForm(){
        document.WebToLeadForm.reset();
    }
    function submit_form(){
        if(typeof(validateCaptchaAndSubmit)!='undefined'){
            validateCaptchaAndSubmit();
        }else{
            check_webtolead_fields();
        }
    }
    function check_webtolead_fields(){
        
        if(document.getElementById('bool_id') != null){
            var reqs=document.getElementById('bool_id').value;
            bools = reqs.substring(0,reqs.lastIndexOf(';'));
            var bool_fields = new Array();
            var bool_fields = bools.split(';');
            nbr_fields = bool_fields.length;
            for(var i=0;i<nbr_fields;i++){
                if(document.getElementById(bool_fields[i]).value == 'on'){
                    document.getElementById(bool_fields[i]).value = 1;
                }
                else{
                    document.getElementById(bool_fields[i]).value = 0;
                }
            }
        }
        if(document.getElementById('req_id') != null){
            var reqs=document.getElementById('req_id').value;
            reqs = reqs.substring(0,reqs.lastIndexOf(';'));
            var req_fields = new Array();
            var req_fields = reqs.split(';');
            nbr_fields = req_fields.length;
            var req = true;
            for(var i=0;i<nbr_fields;i++){
                if(document.getElementById(req_fields[i]).value.length <=0 || document.getElementById(req_fields[i]).value==0){
                    req = false;
                    document.getElementById(req_fields[i]).focus(); 
                    break;
                        }
                else {
                    if(document.getElementById(req_fields[i]).name == 'webtolead_email1') {
                        if(document.getElementById('webtolead_email1').value.match(/^\w+(['\.\-\+]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,})+$/) == null){
                            alert('Not a valid email address');
                            req = false;
                            document.getElementById('webtolead_email1').focus(); 
                            break;
                                }
                    }
                    else {
                        if(document.getElementById(req_fields[i]).name == 'combo0' && document.getElementById(req_fields[i]).value=='value1') {
                            req = false;
                            document.getElementById(req_fields[i]).focus(); 
                            break;
                                }
                    }                
                }
            }
            if(req){
                if (document.getElementById('combo_0').value == 'value2') {
                    document.getElementById('region_code_c').value = 'EUS';
                }
                else {
                    if (document.getElementById('combo_0').value == 'value3') {
                        document.getElementById('region_code_c').value = 'LATAM';
                    }
                    else {
                        if (document.getElementById('combo_0').value == 'value4') {
                            document.getElementById('region_code_c').value = 'EMEA';
                        }
                        else {
                            if (document.getElementById('combo_0').value == 'value5') {
                                document.getElementById('region_code_c').value = 'APAC';
                            }
                            else {
                                if (document.getElementById('combo_0').value == 'value6') {
                                    document.getElementById('region_code_c').value = 'UNKNOWN';
                                }
                            }
                        }
                    }
                }
                document.getElementById('primary_address_country').value = document.getElementById('combo_1').value;
                if (document.getElementById('combo_2').value <= -1 || document.getElementById('combo_2').value == 0) {
                    document.getElementById('primary_address_state').value = '';            
                }
                else {
                    document.getElementById('primary_address_state').value = document.getElementById('combo_2').value;            
                }
                
                document.WebToLeadForm.submit();
                return true;
            }
            else{
                alert('Please provide all the required fields');
                return false;
            }
            return false;
        }
        else{
            document.WebToLeadForm.submit();
        }
    }
    function validateEmailAdd(){
        if(document.getElementById('webtolead_email1').value.length >0) {
            if(document.getElementById('webtolead_email1').value.match(/^\w+(['\.\-\+]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,})+$/) == null){
                alert('Not a valid email address');
                document.getElementById('webtolead_email1').focus(); 
            }
        }
        if(document.getElementById('webtolead_email2').value.length >0) {
            if(document.getElementById('webtolead_email2').value.match(/^\w+(['\.\-\+]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,})+$/) == null){
                alert('Not a valid email address');
                document.getElementById('webtolead_email2').focus(); 
            }
        }
    }
// ]]></script>
<div style="margin: 0 auto;" id="sugar-form-maindiv"><form id="WebToLeadForm" method="post" name="WebToLeadForm" action="https://crm.newtek.com/index.php?entryPoint=WebToLeadCapture">
<div id="col_left"><label>Salutation:</label><br /><select id="salutation" class="formfield" tabindex="1" name="salutation"> <option selected="selected" value="">-none-</option> <option value="Mr.">Mr.</option> <option value="Ms.">Ms.</option> <option value="Mrs.">Mrs.</option> <option value="Dr.">Dr.</option> <option value="Prof.">Prof.</option> <option value="SFC">SFC</option> <option value="MAJ">MAJ</option> <option value="LTC">LTC</option> <option value="MG">MG</option> <option value="CPT">CPT</option></select> <br /><label>First Name: *</label><br /><input id="first_name" class="formfieldtxt" name="first_name" type="text" /> <br /><label>Last Name: *</label><br /><input id="last_name" class="formfieldtxt" name="last_name" type="text" /> <br /><label>Phone (work): *</label><br /><input id="phone_work" class="formfieldtxt" name="phone_work" type="text" /> <br /><label>Phone (mobile): </label><br /><input id="phone_mobile" class="formfieldtxt" name="phone_mobile" type="text" /> <br /><label>Email: *</label><br /><input id="webtolead_email1" class="formfieldtxt" onchange="validateEmailAdd();" name="webtolead_email1" type="text" /> <br /><label>Region: *</label><br /><input id="region_code_c" name="region_code_c" type="hidden" /> <select id="combo_0" class="formfield" onchange="change(this);" name="combo0"> <option selected="selected" value="value1">-select-</option> <option value="value2">US/Canada</option> <option value="value3">Latin America</option> <option value="value4">Europe, Middle East &amp; Africa</option> <option value="value5">Asia Pacific</option></select> <br /><label>Country: *</label><br /><input id="primary_address_country" name="primary_address_country" type="hidden" /> <select id="combo_1" class="formfield" onchange="change(this)" name="combo1"> <option selected="selected" value="value1"></option></select> <br /><label>Company: </label><br /><input id="account_name" class="formfieldtxt" name="account_name" type="text" /> <br /><label>Address: </label><br /><input id="primary_address_street" class="formfieldtxt" name="primary_address_street" type="text" /> <br /><label>City: </label><br /><input id="primary_address_city" class="formfieldtxt" name="primary_address_city" type="text" /> <br /><label>State: </label><br /><input id="primary_address_state" name="primary_address_state" type="hidden" /> <select id="combo_2" class="formfield" onchange="change(this);" name="combo2"> <option selected="selected" value="value1"></option></select> <br /><label>Zip:</label><br /><input id="primary_address_postalcode" class="formfieldtxt" name="primary_address_postalcode" type="text" /> <br /><br /><label>Referred By: </label><br /><input id="refered_by" class="formfieldtxt" name="refered_by" type="text" /></div>
<div id="col_right"><label>Industry:</label><br /><select id="industry_c" class="formfield" name="industry_c"> <option selected="selected" value="">-none-</option> <option value="Aerospace and Defense">Aerospace and Defense</option> <option value="Architectural Visualization">Architectural Visualization</option> <option value="Broadcast">Broadcast</option> <option value="Churches">Churches</option> <option value="Corporate">Corporate</option> <option value="Education">Education</option> <option value="Educational service">Educational service</option> <option value="Enterprise">Enterprise</option> <option value="Film">Film</option> <option value="Games">Games</option> <option value="Government">Government</option> <option value="Healthcare">Healthcare</option> <option value="Hospitality">Hospitality</option> <option value="Independent Film">Independent Film</option> <option value="Manufacturing">Manufacturing</option> <option value="Media">Media</option> <option value="Medical">Medical</option> <option value="Not For Profit">Not For Profit</option> <option value="Other">Other</option> <option value="Print">Print</option> <option value="Radio">Radio</option> <option value="Recreation">Recreation</option> <option value="Retail">Retail</option> <option value="Sports">Sports</option> <option value="Technology">Technology</option> <option value="Telecommunications">Telecommunications</option> <option value="Television">Television</option> <option value="Utilities">Utilities</option> <option value="Worship">Worship</option></select> <br /><label>Industry (if Other):</label><br /><input id="industry_other_c" class="formfieldtxt" name="industry_other_c" type="text" /> <br /><label>Preferred Communication Method:</label><br /><select id="pref_comm_method_c[]" class="formfield" multiple="multiple" name="pref_comm_method_c[]"> <option selected="selected" value="">-none-</option> <option value="Email">Email</option> <option value="Fax">Fax</option> <option value="Mobile">Mobile</option> <option value="Phone">Phone</option></select> <br /><label>Demo Needed: </label><br /><select id="demo_needed_c" class="formfield" name="demo_needed_c"> <option selected="selected" value="Yes">Yes</option> <option value="No">No</option></select> <br /><label>Product Interest:</label><br /><select id="product_interest_c[]" class="formfield" multiple="multiple" name="product_interest_c[]"> <option value="3Play">3Play</option> <option value="TriCaster">TriCaster</option> <option value="LightWave 3D">LightWave 3D</option> <option value="SpeedEDIT">SpeedEDIT</option> <option value="3D Arsenal">3D Arsenal</option> <option value="Accessories">Accessories</option></select> <br /><label>Budget:</label><br /><select id="budget_c" class="formfield" name="budget_c"> <option selected="selected" value="">-none-</option> <option value="Less than 10K">Less than 10,000</option> <option value="10K to 25K">10,000 to 25,000</option> <option value="25K to 50K">25,000 to 50,000</option> <option value="Greater than 50K">Greater than 50,000</option></select> <br /><br /><input class="button" onclick="submit_form();" value="Submit" name="Submit" type="button" /> <input id="campaign_id" value="bdfe397e-24e3-d6c8-0157-4e8e28cda65d" name="campaign_id" type="hidden" /> <!-- default web to lead campaign id: 879e86c1-9424-8730-4ae5-4da36ec63761--><input id="lead_source" value="NewTek.com" name="lead_source" type="hidden" /> <input id="redirect_url" value="http://www.newtek.com" name="redirect_url" type="hidden" /> <input id="assigned_user_id" value="1" name="assigned_user_id" type="hidden" /> <input id="team_id" value="b11b490c-013c-77ff-24d8-4e5d5de668a5" name="team_id" type="hidden" /> <input id="req_id" value="combo_0;combo_1;first_name;last_name;phone_work;webtolead_email1;" name="req_id" type="hidden" /></div>
</form>
<div style="clear: both;"></div>
</div>
<script type="text/javascript">// <![CDATA[
ClearForm();
// ]]></script>
