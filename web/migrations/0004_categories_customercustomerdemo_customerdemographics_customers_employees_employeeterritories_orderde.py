# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20160113_0131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('categoryid', models.AutoField(serialize=False, primary_key=True, db_column=b'CategoryID')),
                ('categoryname', models.CharField(max_length=15, db_column=b'CategoryName')),
                ('description', models.CharField(max_length=250, null=True, db_column=b'Description', blank=True)),
                ('picture', models.TextField(null=True, db_column=b'Picture', blank=True)),
            ],
            options={
                'db_table': 'categories',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customercustomerdemo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'customercustomerdemo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customerdemographics',
            fields=[
                ('customertypeid', models.CharField(max_length=10, serialize=False, primary_key=True, db_column=b'CustomerTypeID')),
                ('customerdesc', models.CharField(max_length=250, null=True, db_column=b'CustomerDesc', blank=True)),
            ],
            options={
                'db_table': 'customerdemographics',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customerid', models.CharField(max_length=5, serialize=False, primary_key=True, db_column=b'CustomerID')),
                ('companyname', models.CharField(max_length=40, db_column=b'CompanyName')),
                ('contactname', models.CharField(max_length=30, null=True, db_column=b'ContactName', blank=True)),
                ('contacttitle', models.CharField(max_length=30, null=True, db_column=b'ContactTitle', blank=True)),
                ('address', models.CharField(max_length=60, null=True, db_column=b'Address', blank=True)),
                ('city', models.CharField(max_length=15, null=True, db_column=b'City', blank=True)),
                ('region', models.CharField(max_length=15, null=True, db_column=b'Region', blank=True)),
                ('postalcode', models.CharField(max_length=10, null=True, db_column=b'PostalCode', blank=True)),
                ('country', models.CharField(max_length=15, null=True, db_column=b'Country', blank=True)),
                ('phone', models.CharField(max_length=24, null=True, db_column=b'Phone', blank=True)),
                ('fax', models.CharField(max_length=24, null=True, db_column=b'Fax', blank=True)),
            ],
            options={
                'db_table': 'customers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('employeeid', models.AutoField(serialize=False, primary_key=True, db_column=b'EmployeeID')),
                ('lastname', models.CharField(max_length=20, db_column=b'LastName')),
                ('firstname', models.CharField(max_length=10, db_column=b'FirstName')),
                ('title', models.CharField(max_length=30, null=True, db_column=b'Title', blank=True)),
                ('titleofcourtesy', models.CharField(max_length=25, null=True, db_column=b'TitleOfCourtesy', blank=True)),
                ('birthdate', models.DateTimeField(null=True, db_column=b'BirthDate', blank=True)),
                ('hiredate', models.DateTimeField(null=True, db_column=b'HireDate', blank=True)),
                ('address', models.CharField(max_length=60, null=True, db_column=b'Address', blank=True)),
                ('city', models.CharField(max_length=15, null=True, db_column=b'City', blank=True)),
                ('region', models.CharField(max_length=15, null=True, db_column=b'Region', blank=True)),
                ('postalcode', models.CharField(max_length=10, null=True, db_column=b'PostalCode', blank=True)),
                ('country', models.CharField(max_length=15, null=True, db_column=b'Country', blank=True)),
                ('homephone', models.CharField(max_length=24, null=True, db_column=b'HomePhone', blank=True)),
                ('extension', models.CharField(max_length=4, null=True, db_column=b'Extension', blank=True)),
                ('photo', models.TextField(null=True, db_column=b'Photo', blank=True)),
                ('notes', models.CharField(max_length=250, null=True, db_column=b'Notes', blank=True)),
                ('reportsto', models.IntegerField(null=True, db_column=b'ReportsTo', blank=True)),
                ('photopath', models.CharField(max_length=255, null=True, db_column=b'PhotoPath', blank=True)),
            ],
            options={
                'db_table': 'employees',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employeeterritories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'employeeterritories',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'DetailID')),
                ('unitprice', models.FloatField(db_column=b'UnitPrice')),
                ('quantity', models.SmallIntegerField(db_column=b'Quantity')),
                ('discount', models.FloatField(db_column=b'Discount')),
            ],
            options={
                'db_table': 'order_details',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('orderid', models.AutoField(serialize=False, primary_key=True, db_column=b'OrderID')),
                ('customerid', models.CharField(max_length=5, null=True, db_column=b'CustomerID', blank=True)),
                ('employeeid', models.IntegerField(null=True, db_column=b'EmployeeID', blank=True)),
                ('orderdate', models.CharField(max_length=50, null=True, db_column=b'OrderDate', blank=True)),
                ('requireddate', models.CharField(max_length=50, null=True, db_column=b'RequiredDate', blank=True)),
                ('shippeddate', models.CharField(max_length=50, null=True, db_column=b'ShippedDate', blank=True)),
                ('shipvia', models.IntegerField(null=True, db_column=b'ShipVia', blank=True)),
                ('freight', models.FloatField(null=True, db_column=b'Freight', blank=True)),
                ('shipname', models.CharField(max_length=40, null=True, db_column=b'ShipName', blank=True)),
                ('shipaddress', models.CharField(max_length=60, null=True, db_column=b'ShipAddress', blank=True)),
                ('shipcity', models.CharField(max_length=15, null=True, db_column=b'ShipCity', blank=True)),
                ('shipregion', models.CharField(max_length=15, null=True, db_column=b'ShipRegion', blank=True)),
                ('shippostalcode', models.CharField(max_length=10, null=True, db_column=b'ShipPostalCode', blank=True)),
                ('shipcountry', models.CharField(max_length=15, null=True, db_column=b'ShipCountry', blank=True)),
            ],
            options={
                'db_table': 'orders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('productid', models.AutoField(serialize=False, primary_key=True, db_column=b'ProductID')),
                ('productname', models.CharField(max_length=40, db_column=b'ProductName')),
                ('supplierid', models.IntegerField(null=True, db_column=b'SupplierID', blank=True)),
                ('categoryid', models.IntegerField(null=True, db_column=b'CategoryID', blank=True)),
                ('quantityperunit', models.CharField(max_length=20, null=True, db_column=b'QuantityPerUnit', blank=True)),
                ('unitprice', models.FloatField(null=True, db_column=b'UnitPrice', blank=True)),
                ('unitsinstock', models.SmallIntegerField(null=True, db_column=b'UnitsInStock', blank=True)),
                ('unitsonorder', models.SmallIntegerField(null=True, db_column=b'UnitsOnOrder', blank=True)),
                ('reorderlevel', models.SmallIntegerField(null=True, db_column=b'ReorderLevel', blank=True)),
                ('discontinued', models.TextField(db_column=b'Discontinued')),
            ],
            options={
                'db_table': 'products',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('regionid', models.IntegerField(serialize=False, primary_key=True, db_column=b'RegionID')),
                ('regiondescription', models.CharField(max_length=50, db_column=b'RegionDescription')),
            ],
            options={
                'db_table': 'region',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Shippers',
            fields=[
                ('shipperid', models.AutoField(serialize=False, primary_key=True, db_column=b'ShipperID')),
                ('companyname', models.CharField(max_length=40, db_column=b'CompanyName')),
                ('phone', models.CharField(max_length=24, null=True, db_column=b'Phone', blank=True)),
            ],
            options={
                'db_table': 'shippers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('supplierid', models.AutoField(serialize=False, primary_key=True, db_column=b'SupplierID')),
                ('companyname', models.CharField(max_length=40, db_column=b'CompanyName')),
                ('contactname', models.CharField(max_length=30, null=True, db_column=b'ContactName', blank=True)),
                ('contacttitle', models.CharField(max_length=30, null=True, db_column=b'ContactTitle', blank=True)),
                ('address', models.CharField(max_length=60, null=True, db_column=b'Address', blank=True)),
                ('city', models.CharField(max_length=15, null=True, db_column=b'City', blank=True)),
                ('region', models.CharField(max_length=15, null=True, db_column=b'Region', blank=True)),
                ('postalcode', models.CharField(max_length=10, null=True, db_column=b'PostalCode', blank=True)),
                ('country', models.CharField(max_length=15, null=True, db_column=b'Country', blank=True)),
                ('phone', models.CharField(max_length=24, null=True, db_column=b'Phone', blank=True)),
                ('fax', models.CharField(max_length=24, null=True, db_column=b'Fax', blank=True)),
                ('homepage', models.CharField(max_length=250, null=True, db_column=b'HomePage', blank=True)),
            ],
            options={
                'db_table': 'suppliers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Territories',
            fields=[
                ('territoryid', models.CharField(max_length=20, serialize=False, primary_key=True, db_column=b'TerritoryID')),
                ('territorydescription', models.CharField(max_length=50, db_column=b'TerritoryDescription')),
            ],
            options={
                'db_table': 'territories',
                'managed': False,
            },
        ),
    ]
