require 'test_helper'

class CustomersControllerTest < ActionController::TestCase
  setup do
    @customer = customers(:one)
  end

  test "should get index" do
    get :index
    assert_response :success
    assert_not_nil assigns(:customers)
  end

  test "should get new" do
    get :new
    assert_response :success
  end

  test "should create customer" do
    assert_difference('Customer.count') do
      post :create, customer: { age_group: @customer.age_group, child_age_group: @customer.child_age_group, customer_firstName: @customer.customer_firstName, customer_id: @customer.customer_id, customer_lastName: @customer.customer_lastName, customer_relationship: @customer.customer_relationship, district: @customer.district, gender: @customer.gender, has_child: @customer.has_child, mobile_number: @customer.mobile_number, postcode: @customer.postcode, province: @customer.province, street_name: @customer.street_name, street_number: @customer.street_number }
    end

    assert_redirected_to customer_path(assigns(:customer))
  end

  test "should show customer" do
    get :show, id: @customer
    assert_response :success
  end

  test "should get edit" do
    get :edit, id: @customer
    assert_response :success
  end

  test "should update customer" do
    patch :update, id: @customer, customer: { age_group: @customer.age_group, child_age_group: @customer.child_age_group, customer_firstName: @customer.customer_firstName, customer_id: @customer.customer_id, customer_lastName: @customer.customer_lastName, customer_relationship: @customer.customer_relationship, district: @customer.district, gender: @customer.gender, has_child: @customer.has_child, mobile_number: @customer.mobile_number, postcode: @customer.postcode, province: @customer.province, street_name: @customer.street_name, street_number: @customer.street_number }
    assert_redirected_to customer_path(assigns(:customer))
  end

  test "should destroy customer" do
    assert_difference('Customer.count', -1) do
      delete :destroy, id: @customer
    end

    assert_redirected_to customers_path
  end
end
