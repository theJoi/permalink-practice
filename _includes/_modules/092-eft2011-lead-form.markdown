---
layout: module
title: EFT2011 Lead Form
joomla_module_id: 92
position: EFT2011-sugarform
---
<script src="/includes/js/regionCountryState.js" type="text/javascript"></script>
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
<div id="sugar-form-maindiv" style="margin: 0 auto;"><form action="https://crm.newtek.com/index.php?entryPoint=WebToLeadCapture" name="WebToLeadForm" method="POST" id="WebToLeadForm">
<div id="col_left"><label>Salutation:</label><br /> <select name="salutation" class="formfield" id="salutation" tabindex="1"> <option selected="selected" value="">-none-</option> <option value="Mr.">Mr.</option> <option value="Ms.">Ms.</option> <option value="Mrs.">Mrs.</option> <option value="Dr.">Dr.</option> <option value="Prof.">Prof.</option> <option value="SFC">SFC</option> <option value="MAJ">MAJ</option> <option value="LTC">LTC</option> <option value="MG">MG</option> <option value="CPT">CPT</option></select> <br /> <label>First Name: *</label><br /> <input name="first_name" class="formfieldtxt" id="first_name" type="text" /> <br /> <label>Last Name: *</label><br /> <input name="last_name" class="formfieldtxt" id="last_name" type="text" /> <br /> <label>Phone (work): *</label><br /> <input name="phone_work" class="formfieldtxt" id="phone_work" type="text" /> <br /> <label>Phone (mobile): </label><br /> <input name="phone_mobile" class="formfieldtxt" id="phone_mobile" type="text" /> <br /> <label>Email: *</label><br /> <input name="webtolead_email1" class="formfieldtxt" id="webtolead_email1" onchange="validateEmailAdd();" type="text" /> <br /> <label>Region: *</label><br /> <input name="region_code_c" id="region_code_c" type="hidden" /> <select class="formfield" name="combo0" id="combo_0" onchange="change(this);"> <option value="value1">-select-</option> <option value="value2">US/Canada</option> <option value="value3">Latin America</option> <option value="value4">Europe, Middle East &amp; Africa</option> <option value="value5">Asia Pacific</option> </select> <br /> <label>Country: *</label><br /> <input name="primary_address_country" id="primary_address_country" type="hidden" /> <select class="formfield" name="combo1" id="combo_1" onchange="change(this)"> <option value="value1"> </option> </select> <br /> <label>Company: </label><br /> <input name="account_name" class="formfieldtxt" id="account_name" type="text" /> <br /> <label>Address: </label><br /> <input name="primary_address_street" class="formfieldtxt" id="primary_address_street" type="text" /> <br /> <label>City: </label><br /> <input name="primary_address_city" class="formfieldtxt" id="primary_address_city" type="text" /> <br /> <label>State: </label><br /> <input name="primary_address_state" id="primary_address_state" type="hidden" /> <select class="formfield" name="combo2" id="combo_2" onchange="change(this);"> <option value="value1"> </option> </select> <br /> <label>Zip:</label><br /> <input name="primary_address_postalcode" class="formfieldtxt" id="primary_address_postalcode" type="text" /> <br /> <br /> <label>Referred By: </label><br /> <input name="refered_by" class="formfieldtxt" id="refered_by" type="text" /></div>
<div id="col_right"><label>Industry:</label><br /> <select name="industry_c" class="formfield" id="industry_c"> <option selected="selected" value="">-none-</option> <option value="Aerospace and Defense">Aerospace and Defense</option> <option value="Architectural Visualization">Architectural Visualization</option> <option value="Broadcast">Broadcast</option> <option value="Churches">Churches</option> <option value="Corporate">Corporate</option> <option value="Education">Education</option> <option value="Educational service">Educational service</option> <option value="Enterprise">Enterprise</option> <option value="Film">Film</option> <option value="Games">Games</option> <option value="Government">Government</option> <option value="Healthcare">Healthcare</option> <option value="Hospitality">Hospitality</option> <option value="Independent Film">Independent Film</option> <option value="Manufacturing">Manufacturing</option> <option value="Media">Media</option> <option value="Medical">Medical</option> <option value="Not For Profit">Not For Profit</option> <option value="Other">Other</option> <option value="Print">Print</option> <option value="Radio">Radio</option> <option value="Recreation">Recreation</option> <option value="Retail">Retail</option> <option value="Sports">Sports</option> <option value="Technology">Technology</option> <option value="Telecommunications">Telecommunications</option> <option value="Television">Television</option> <option value="Utilities">Utilities</option> <option value="Worship">Worship</option></select> <br /> <label>Industry (if Other):</label><br /> <input name="industry_other_c" class="formfieldtxt" id="industry_other_c" type="text" /> <br /> <label>Preferred Communication Method:</label><br /> <select name="pref_comm_method_c[]" multiple="multiple" class="formfield" id="pref_comm_method_c[]"> <option selected="selected" value="">-none-</option> <option value="Email">Email</option> <option value="Fax">Fax</option> <option value="Mobile">Mobile</option> <option value="Phone">Phone</option></select> <br /> <label>Demo Needed: </label><br /> <select name="demo_needed_c" class="formfield" id="demo_needed_c"> <option selected="selected" value="Yes">Yes</option> <option value="No">No</option></select> <br /> <label>Product Interest:</label><br /> <select name="product_interest_c[]" multiple="multiple" class="formfield" id="product_interest_c[]"> <option value="3Play">3Play</option> <option value="TriCaster">TriCaster</option> <option value="LightWave 3D">LightWave 3D</option> <option value="SpeedEDIT">SpeedEDIT</option> <option value="3D Arsenal">3D Arsenal</option> <option value="Accessories">Accessories</option></select> <br /> <label>Budget:</label><br /> <select name="budget_c" class="formfield" id="budget_c"> <option selected="selected" value="">-none-</option> <option value="Less than 10K">Less than 10,000</option> <option value="10K to 25K">10,000 to 25,000</option> <option value="25K to 50K">25,000 to 50,000</option> <option value="Greater than 50K">Greater than 50,000</option></select> <br /> <br /> <input onclick="submit_form();" class="button" name="Submit" value="Submit" type="button" /> <input id="campaign_id" name="campaign_id" value="9b22b70d-fddc-44c3-ce05-4e6108ed6575" type="hidden" /> <!-- default web to lead campaign id: 879e86c1-9424-8730-4ae5-4da36ec63761--> <input id="lead_source" name="lead_source" value="NewTek.com" type="hidden" /> <input id="redirect_url" name="redirect_url" value="http://www.newtek.com" type="hidden" /> <input id="assigned_user_id" name="assigned_user_id" value="1" type="hidden" /> <input id="team_id" name="team_id" value="b11b490c-013c-77ff-24d8-4e5d5de668a5" type="hidden" /> <input id="req_id" name="req_id" value="combo_0;combo_1;first_name;last_name;phone_work;webtolead_email1;" type="hidden" /></div>
</form>
<div style="clear: both;"></div>
</div>
<script type="text/javascript">// <![CDATA[
ClearForm();
// ]]></script>
