class AddOrderToCustomer < ActiveRecord::Migration
  def change
    add_foreign_key :order, :customer
  end
end
