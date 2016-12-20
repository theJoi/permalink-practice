<?php defined('_JEXEC') or die('Restricted access'); ?>

<!--
 -- Layout:  Product Downloads
 -- File:    templates/newtekv2/layouts/product-downloads.php
 -- Styles:  templates/newtekv2/css/layouts/downloads.css
 -- Author:  Ryan Goree
 -- Created: 10/05/2015
 -->
<div id="contentwrap">
	<div id="content" class="clearfix">
		<div id="main" class="clearfix <?php echo $style; ?>">

			<?php if($this->countModules('sticky-nav')) : ?>
				<div class="sticky-nav-container">

					<!-- include module position: sticky-nav -->
					<jdoc:include type="modules" name="sticky-nav" />

				</div>
				<script src="<?php echo $this->baseurl; ?>/templates/<?php echo $this->template; ?>/js/sticky-nav.js"></script>
			<?php endif; ?>

			<?php if ($this->countModules('banner')) : ?>
			<div class="banner-container clearfix">

				<!-- include module position: banner -->
				<jdoc:include type="modules" name="banner" />

			</div>
			<?php endif; ?>

			<!-- include component -->
			<jdoc:include type="component" />

			<?php if ($this->countModules('product-list')) : ?>
			<div class="product-list-container buckets-large clearfix">

				<!-- include module position: product-list -->
				<jdoc:include type="modules" name="product-list" />

			</div>
			<script>
				$(window).load(function() {
					var productImages = document.querySelectorAll('.product-list-container .header-img-container');
					var productContent = document.querySelectorAll('.product-list-container .bucket-content');
					for (var i=0; i<productImages.length; i+=2) {
						var rowImages = [
							productImages[i],
							productImages[i+1]
						];
						var rowContent = [
							productContent[i],
							productContent[i+1]
						]
						NEWTEKV2.equal_heights(rowImages);
						NEWTEKV2.equal_heights(rowContent);
					}
				});
			</script>
			<?php endif; ?>
			<?php if ($this->countModules('aside') && $this->countModules('form')) : ?>
			<div class="aside-form-combo clearfix aside-cols-<?php echo $this->countModules('aside'); ?>">
			<?php elseif ($this->countModules('aside')) : ?>
			<div class="aside-only clearfix aside-cols-<?php echo $this->countModules('aside'); ?>">
			<?php endif; ?>

				<?php
				if ($this->countModules('aside')) :
					$aside_modules = JModuleHelper::getModules('aside');
					$attribs['style'] = 'html';
					$i = 0;
					foreach ($aside_modules as $aside) {
						$i++;
				?>
				<div id="aside-<?php echo $i ?>" class="aside-container">
					<?php echo JModuleHelper::renderModule($aside, $attribs); ?>
				</div>
				<?php
					}
				endif;
				?>

				<?php if ($this->countModules('form')) : ?>
				<div id="form" class="form-container">

					<!-- include module position: form -->
					<jdoc:include type="modules" name="form" />

				</div>


				<?php endif; ?>

				<?php if ($this->countModules('aside') && $this->countModules('form')) : ?>
				<script>
					$(window).load(function() {
						NEWTEKV2.equal_heights('<?php
							$i = 0;
							foreach ($aside_modules as $aside) {
								$i++;
								echo 'aside-' . $i . ',';
							}
						?>form');
					});
				</script>
				<?php elseif ($this->countModules('aside')) : ?>
				<script>
					$(window).load(function() {
						NEWTEKV2.equal_heights('<?php
							$i = 0;
							foreach ($aside_modules as $aside) {
								$i++;
								echo 'aside-' . $i . ',';
							}
						?>form');
					});
				</script>
				<?php endif; ?>



			<?php if ($this->countModules('stories')) : ?>
			<div class="stories-container clearfix">

				<!-- include module position: stories -->
				<jdoc:include type="modules" name="stories" />

			</div>
			<script>
				$(window).load(function() {
					NEWTEKV2.equal_heights(document.querySelectorAll('.srfrThumb'));
					NEWTEKV2.equal_heights(document.querySelectorAll('.srfrRow'));
				});
			</script>
			<?php endif; ?>

		</div>
	</div>
</div>
