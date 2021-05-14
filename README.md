# Ship-O-Cereal
####Assignment for T-220-VLN2 2021

### Hosting
The site can be accessed online at https://ship-o-cereal.herokuapp.com/ \
and on Github at https://github.com/stebbilax/VLN2-2021-H32

### Additional Requirements
- The user can reset their password through email confirmation
- A user can choose to store their payment information in the checkout menu, enabling their checkout form to be pre-populated at their next checkout.
- All cart and checkout functionality is available to a user without an account.
- A logged-out user will have their cart information persist through their browser being closed, and the information will be linked to the device they are using
- The user has the option to contact website staff through a contact form.
- Several features utilize javascript in preventing a page reload to make the user experience more seamless and smooth. These include product filtering/ordering, cart manipulation and movement between the different stages of checkout.
- The navbar displays a dynamic number of items a user has added to their cart.
- All static assets are stored and served from an Amazon AWS bucket.
- Automated tests were written for models and views across the apps.
- A confirmation email is sent to a user with an account on completion of the checkout phase.


### App Hierarchy
* Account \
├ (Models) Account | PaymentInfo | SearchHistoryEntry  \
├ (Decorators) check_if_user_exists \
├ (Forms) CreateUserForm | LoginForm | EditAccountForm | UserPasswordResetForm | UserSetPasswordForm \
├ (Signals) create_account \
├ (Views)  account_page | login_page | search_history_page | logout_user | create_account | delete_account
* Cart \
├ (Models) Cart | CartItem \
├ (Decorators) check_item_owner | collect_cart_info \
├ (Signals) create_cart \
├ (Views)  cart_page | get_summary_info | increase_quantity | decrease_quantity | get_item_count | remove_item 
* Order \
├ (Models) Order | OrderContains \
├ (Decorators) make_order \
├ (Forms) PaymentInfoForm \
├ (Utils) create_order | create_payment_info | send_confirmation_email \
├ (Views)  checkout_page
* User \
├ (Models) Category | Product | Keyword | ProductPhoto \
├ (Decorators) record_search_history \
├ (Forms) ContactEmailForm \
├ (Views)  index | about_us_page | contact_us_page | products_page | product_page | get_product_data | get_keywords 