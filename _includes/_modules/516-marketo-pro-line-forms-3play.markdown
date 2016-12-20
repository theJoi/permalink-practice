---
layout: module
title: Marketo - Pro Line Forms (3Play)
joomla_module_id: 516
position: rightside
---
<script type="text/javascript">// <![CDATA[
$(document).ready(function(){
            //
			//alert('hej!');
			$('.prospects').hide();
			$('.existing').hide();
			//
			$('.prospects-btn').click(function(){
				$('.existing').hide();
				$('.prospects').slideDown(1500, 'linear');
			});
			$('.existing-btn').click(function(){
				$('.prospects').hide();
				$('.existing').slideDown(1500, 'linear');
			});
});
// ]]></script>
{loadposition marketo-form}
