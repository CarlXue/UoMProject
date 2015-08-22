class AddReferenceToOrders < ActiveRecord::Migration
  def change
    add_foreign_key :products, :orders
    add_foreign_key :customers, :orders
  end
end
