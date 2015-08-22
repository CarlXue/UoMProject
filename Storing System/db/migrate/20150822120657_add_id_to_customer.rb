class AddIdToCustomer < ActiveRecord::Migration
  def change
    add_column :customers, :IDNumber, :text

  end
end
