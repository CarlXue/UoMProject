require 'test_helper'

class OrdersControllerTest < ActionController::TestCase
  setup do
    @order = orders(:one)
  end

  test "should get index" do
    get :index
    assert_response :success
    assert_not_nil assigns(:orders)
  end

  test "should get new" do
    get :new
    assert_response :success
  end

  test "should create order" do
    assert_difference('Order.count') do
      post :create, order: { customer_id: @order.customer_id, delivery_fee_rmb: @order.delivery_fee_rmb, discount: @order.discount, order_date: @order.order_date, order_id: @order.order_id, product_id: @order.product_id, product_quantity: @order.product_quantity, total_cost_rmb: @order.total_cost_rmb, total_price_rmb: @order.total_price_rmb, unit_price_rmb: @order.unit_price_rmb }
    end

    assert_redirected_to order_path(assigns(:order))
  end

  test "should show order" do
    get :show, id: @order
    assert_response :success
  end

  test "should get edit" do
    get :edit, id: @order
    assert_response :success
  end

  test "should update order" do
    patch :update, id: @order, order: { customer_id: @order.customer_id, delivery_fee_rmb: @order.delivery_fee_rmb, discount: @order.discount, order_date: @order.order_date, order_id: @order.order_id, product_id: @order.product_id, product_quantity: @order.product_quantity, total_cost_rmb: @order.total_cost_rmb, total_price_rmb: @order.total_price_rmb, unit_price_rmb: @order.unit_price_rmb }
    assert_redirected_to order_path(assigns(:order))
  end

  test "should destroy order" do
    assert_difference('Order.count', -1) do
      delete :destroy, id: @order
    end

    assert_redirected_to orders_path
  end
end
