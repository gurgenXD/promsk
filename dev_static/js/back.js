$(document).ready(function(){
    $('#ContactModal button[type="submit"]').on('click', function(e) {
        e.preventDefault();
        $(this).prop('disabled', true);

        name = $('#ContactModal input[name="name"]').val();
        email_or_phone = $('#ContactModal input[name="email_or_phone"]').val();
        text = $('#ContactModal textarea[name="text"]').val();
        csrf_token = $('#ContactModal input[name="csrfmiddlewaretoken"]').val();

        data = {
            'csrfmiddlewaretoken': csrf_token,
            name: name,
            email_or_phone: email_or_phone,
            text: text,
        }

        $.ajax({
        	type: 'POST',
        	url: $('#ContactModal form').attr('action'),
        	data: data,
            success: function(data) {
                if (data.status) {
                    $('#ContactModal .modal-success').removeClass('d-none');
                    $('#ContactModal .modal-success').addClass('d-flex');
                } else {
                    $('#ContactModal .alert-danger').removeClass('d-none');
                }
        	}
        });
    });

    $('#CallBackModal button[type="submit"]').on('click', function(e) {
        e.preventDefault();
        $(this).prop('disabled', true);

        phone = $('#CallBackModal input[name="phone"]').val();
        name = $('#CallBackModal input[name="name"]').val();
        csrf_token = $('#CallBackModal input[name="csrfmiddlewaretoken"]').val();

        data = {
            'csrfmiddlewaretoken': csrf_token,
            phone: phone,
            name: name,
        }

        $.ajax({
        	type: 'POST',
        	url: $('#CallBackModal form').attr('action'),
        	data: data,
            success: function(data) {
                if (data.status) {
                    $('#CallBackModal .modal-success').removeClass('d-none');
                    $('#CallBackModal .modal-success').addClass('d-flex');
                } else {
                    $('#CallBackModal .alert-danger').removeClass('d-none');
                }
        	}
        });
    });

    $('#CallBackIndex button[type="submit"]').on('click', function(e) {
        e.preventDefault();
        $(this).prop('disabled', true);

        phone = $('#CallBackIndex input[name="phone"]').val();
        name = $('#CallBackIndex input[name="name"]').val();
        csrf_token = $('#CallBackIndex input[name="csrfmiddlewaretoken"]').val();

        data = {
            'csrfmiddlewaretoken': csrf_token,
            phone: phone,
            name: name,
        }

        $.ajax({
        	type: 'POST',
        	url: $('#CallBackIndex form').attr('action'),
        	data: data,
            success: function(data) {
                if (data.status) {
                    $('#CallBackIndex .form-success').removeClass('d-none');
                    $('#CallBackIndex .form-success').addClass('d-flex');
                } else {
                    $('#CallBackIndex .alert-danger').removeClass('d-none');
                }
        	}
        });
    });

    $('#OrderModal button[type="submit"]').on('click', function(e) {
        e.preventDefault();
        $(this).prop('disabled', true);

        phone = $('#OrderModal input[name="phone"]').val();
        email = $('#OrderModal input[name="email"]').val();
        name = $('#OrderModal input[name="name"]').val();
        text = $('#OrderModal textarea[name="text"]').val();
        product_id = $(this).data('product');
        csrf_token = $('#OrderModal input[name="csrfmiddlewaretoken"]').val();

        data = {
            'csrfmiddlewaretoken': csrf_token,
            phone: phone,
            name: name,
            email: email,
            text: text,
            product_id: product_id,
        };

        $.ajax({
        	type: 'POST',
        	url: $('#OrderModal form').attr('action'),
        	data: data,
            success: function(data) {
                if (data.status) {
                    $('#OrderModal .modal-success').removeClass('d-none');
                    $('#OrderModal .modal-success').addClass('d-flex');
                } else {
                    $('#OrderModal .alert-danger').removeClass('d-none');
                }
        	}
        });
    });
});