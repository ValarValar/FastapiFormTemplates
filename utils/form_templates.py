registration_form_template = {
    "Form template name": "Registration template",
    "template": {
        "username": "text",
        "user_email": "email",
        "user_phone": "phone",
        "user_registration_date": "date",
    }
}

auth_form_template = {
    "Form template name": "Login template",
    "template": {
        "username": "text",
        "password": "text",
    }
}
auth_form_with_email = {
    "Form template name": "Login with email template",
    "template": {
        "username": "text",
        "password": "text",
        "user_email": "email"
    }
}

order_form_template = {
    "Form template name": "Order template",
    "template": {
        "username": "text",
        "user_phone": "phone",
        "order_id": "text",
        "order_date": "date"
    }
}

all_templates = [registration_form_template, auth_form_template, order_form_template, auth_form_with_email]
