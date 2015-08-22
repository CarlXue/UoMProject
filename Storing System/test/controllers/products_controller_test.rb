require 'test_helper'

class ProductsControllerTest < ActionController::TestCase
  setup do
    @product = products(:one)
  end

  test "should get index" do
    get :index
    assert_response :success
    assert_not_nil assigns(:products)
  end

  test "should get new" do
    get :new
    assert_response :success
  end

  test "should create product" do
    assert_difference('Product.count') do
      post :create, product: { cost_aud: @product.cost_aud, cost_rmb: @product.cost_rmb, margin_aud: @product.margin_aud, margin_rmb: @product.margin_rmb, product_brand: @product.product_brand, product_description: @product.product_description, product_id: @product.product_id, product_name: @product.product_name, product_standard: @product.product_standard, stock_au: @product.stock_au, stock_cn: @product.stock_cn, unit_price_aud: @product.unit_price_aud, unit_price_rmb: @product.unit_price_rmb }
    end

    assert_redirected_to product_path(assigns(:product))
  end

  test "should show product" do
    get :show, id: @product
    assert_response :success
  end

  test "should get edit" do
    get :edit, id: @product
    assert_response :success
  end

  test "should update product" do
    patch :update, id: @product, product: { cost_aud: @product.cost_aud, cost_rmb: @product.cost_rmb, margin_aud: @product.margin_aud, margin_rmb: @product.margin_rmb, product_brand: @product.product_brand, product_description: @product.product_description, product_id: @product.product_id, product_name: @product.product_name, product_standard: @product.product_standard, stock_au: @product.stock_au, stock_cn: @product.stock_cn, unit_price_aud: @product.unit_price_aud, unit_price_rmb: @product.unit_price_rmb }
    assert_redirected_to product_path(assigns(:product))
  end

  test "should destroy product" do
    assert_difference('Product.count', -1) do
      delete :destroy, id: @product
    end

    assert_redirected_to products_path
  end
end
