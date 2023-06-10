/*price range*/
 $('#sl2').slider();
	var RGBChange = function() {
	  $('#RGB').css('background', 'rgb('+r.getValue()+','+g.getValue()+','+b.getValue()+')')
	};		
/*scroll to top*/
$(document).ready(function(){
	$(function () {
		$.scrollUp({
	        scrollName: 'scrollUp', // Element ID
	        scrollDistance: 300, // Distance from top/bottom before showing element (px)
	        scrollFrom: 'top', // 'top' or 'bottom'
	        scrollSpeed: 300, // Speed back to top (ms)
	        easingType: 'linear', // Scroll to top easing (see http://easings.net/)
	        animation: 'fade', // Fade, slide, none
	        animationSpeed: 200, // Animation in speed (ms)
	        scrollTrigger: false, // Set a custom triggering element. Can be an HTML string or jQuery object
					//scrollTarget: false, // Set a custom target element for scrolling to the top
	        scrollText: '<i class="fa fa-angle-up"></i>', // Text for element, can contain HTML
	        scrollTitle: false, // Set a custom <a> title if required.
	        scrollImg: false, // Set true to use image
	        activeOverlay: false, // Set CSS color to display scrollUp active point, e.g '#00FFFF'
	        zIndex: 2147483647 // Z-Index for the overlay
		});
	});

	$(document).on('click','#add_to_wishlist', function(e) {
		$('#modal_tital').text('Under construction');
		$('#modal_text').text('We are sorry, but are add this funcanility Now');
		$('#issue_modal').modal('show');
	});

	$(document).on('click', '.btn-close', function(e) {
		$('#issue_modal').modal('hide');
	});

	$(document).on('click', '#forgot_password', function(e) {
		$('#forgot_password_modal').modal('show');
	});

	$(document).on('click', '#forgot_password_close', function(e) {
		$('#forgot_password_modal').modal('hide');
	});
	
	$(document).on('click', '#profile', function(e) {
		$('#profile_modal').modal('show');
	});

	$(document).on('click', '#cart_btn', function(e) {
		var qty = $('#qty').val();
		var new_qty ='';
		if (qty > 0){
			new_qty = (parseInt(qty) - 1);
		}
		var qty = $('#qty').val(new_qty);	
	});

	$(document).on('click', '#change_password', function(e) {
		$('#change_password_modal').modal('show');
	});

	$(document).on('click', '#change_password_close', function(e) {
		$('#change_password_modal').modal('hide');
	});
	$(document).on('click', '.quantity_up', function(e) {
		e.preventDefault();
		var cart_item_id = $(this).attr('data');
		var input_id = "quantity_"+cart_item_id;
		var quantity = $('#'+input_id).val();
		 quantity++
		$('#'+input_id).val(quantity);

	});
	$(document).on('click', '.quantity_down', function(e) {
		e.preventDefault();
		var cart_item_id = $(this).attr('data');
		var input_id = "quantity_"+cart_item_id;
		var quantity = $('#'+input_id).val();
		if (quantity > 1){
			var new_qty = quantity--
			$('#'+input_id).val(quantity);

		}
		
	});
	
	$(document).on('click', '.cart_delete_item', function(e) {
		e.preventDefault();
		var cart_item_id = $(this).attr('data');
		var cart_item = "cart_item_"+cart_item_id;
		$('#'+cart_item).hide();
		delete_CartItem(cart_item_id)		
	});

	function delete_CartItem(id){
		$.ajax({
			url : "/delete_cart_item/"+id,			
			type : 'post',
			success : function(response) {
				$(inputQuantityElement).val(new_quantity);
			}
		});
	}



	function save_to_db(cart_id, new_quantity) {
		var inputQuantityElement = $("#input-quantity-"+cart_id);
		$.ajax({
			url : "update_cart_quantity",
			data : "cart_id="+cart_id+"&new_quantity="+new_quantity,
			type : 'post',
			success : function(response) {
				$(inputQuantityElement).val(new_quantity);
			}
		});
	}
});
