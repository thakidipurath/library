from customer import views
from django.urls import path


urlpatterns = [
    # path('home/', views.index),
    # path('carts/',views.view_my_cart),
    # path('order/',views.view_my_orders),
    # path('feedback/',views.FeedbackView.as_view()),
    path('home/',views.CustmerHome.as_view(),name="custhome"),
    path('accounts/signup/',views.SignupView.as_view(),name="signup"),
    path('accounts/signin/',views. SigninView.as_view(),name="signin"),
    path('account/signout',views.sign_out,name="signout"),
    path('customer/cart/<int:id>',views.Addtocart.as_view(),name="addtocart"),
    path('customer/cartitems',views.CartItems.as_view(),name="cartitem"),
    path('customer/removeitems/<int:id>',views.RemoveCsrtItem.as_view(),name="removecart"),
    path('customer/order/<int:c_id>/<int:p_id>',views.OrderView.as_view(),name="order"),
    path('customer/myorder',views.MyOrders.as_view(),name="myorder"),
    path('customer/cancell/<int:o_id>',views.cancell_order,name="cancelled"),
    path('profile/add',views.ProfileView.as_view(),name="custprofile"),
    path('my/profile',views.ViewMyProfile.as_view(),name="myprofile"),

]