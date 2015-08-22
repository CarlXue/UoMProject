require 'test_helper'

class ReportsControllerTest < ActionController::TestCase
  test "should get generate_order_4z-customer" do
    get :generate_order_4z-customer
    assert_response :success
  end

  test "should get generate_order_4_operator" do
    get :generate_order_4_operator
    assert_response :success
  end

end
