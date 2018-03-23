# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('add_date', models.DateTimeField(auto_now=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('desc', tinymce.models.HTMLField(blank=True, default='', verbose_name='详细介绍')),
            ],
            options={
                'verbose_name_plural': '商品',
                'verbose_name': '商品',
                'db_table': 'df_goods',
            },
        ),
        migrations.CreateModel(
            name='GoodsCategory',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('add_date', models.DateTimeField(auto_now=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=20, verbose_name='名称')),
                ('logo', models.CharField(max_length=100, verbose_name='标识')),
                ('image', models.ImageField(upload_to='category', verbose_name='图片')),
            ],
            options={
                'verbose_name_plural': '商品类别',
                'verbose_name': '商品类别',
                'db_table': 'df_goods_category',
            },
        ),
        migrations.CreateModel(
            name='GoodsImage',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('add_date', models.DateTimeField(auto_now=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='goods', verbose_name='图片')),
            ],
            options={
                'verbose_name_plural': '商品图片',
                'verbose_name': '商品图片',
                'db_table': 'df_goods_image',
            },
        ),
        migrations.CreateModel(
            name='GoodsSKU',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('add_date', models.DateTimeField(auto_now=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('title', models.CharField(max_length=200, verbose_name='简介')),
                ('unit', models.CharField(max_length=10, verbose_name='销售单位')),
                ('price', models.DecimalField(max_digits=10, decimal_places=2, verbose_name='价格')),
                ('stock', models.IntegerField(verbose_name='库存', default=0)),
                ('sales', models.IntegerField(verbose_name='销量', default=0)),
                ('default_image', models.ImageField(upload_to='goods', verbose_name='图片')),
                ('status', models.BooleanField(default=True, verbose_name='是否上线')),
                ('category', models.ForeignKey(to='tt_goods.GoodsCategory', verbose_name='类别')),
                ('goods', models.ForeignKey(to='tt_goods.Goods', verbose_name='商品')),
            ],
            options={
                'verbose_name_plural': '商品SKU',
                'verbose_name': '商品SKU',
                'db_table': 'df_goods_sku',
            },
        ),
        migrations.CreateModel(
            name='IndexCategoryGoodsBanner',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('add_date', models.DateTimeField(auto_now=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('display_type', models.SmallIntegerField(choices=[(0, '标题'), (1, '图片')], verbose_name='展示类型')),
                ('index', models.SmallIntegerField(verbose_name='顺序', default=0)),
                ('category', models.ForeignKey(to='tt_goods.GoodsCategory', verbose_name='商品类别')),
                ('sku', models.ForeignKey(to='tt_goods.GoodsSKU', verbose_name='商品SKU')),
            ],
            options={
                'verbose_name_plural': '主页分类展示商品',
                'verbose_name': '主页分类展示商品',
                'db_table': 'df_index_category_goods',
            },
        ),
        migrations.CreateModel(
            name='IndexGoodsBanner',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('add_date', models.DateTimeField(auto_now=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='banner', verbose_name='图片')),
                ('index', models.SmallIntegerField(verbose_name='顺序', default=0)),
                ('sku', models.ForeignKey(to='tt_goods.GoodsSKU', verbose_name='商品SKU')),
            ],
            options={
                'verbose_name_plural': '主页轮播商品',
                'verbose_name': '主页轮播商品',
                'db_table': 'df_index_goods',
            },
        ),
        migrations.CreateModel(
            name='IndexPromotionBanner',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('add_date', models.DateTimeField(auto_now=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=50, verbose_name='活动名称')),
                ('url', models.URLField(verbose_name='活动连接')),
                ('image', models.ImageField(upload_to='banner', verbose_name='图片')),
                ('index', models.SmallIntegerField(verbose_name='顺序', default=0)),
            ],
            options={
                'verbose_name_plural': '主页促销活动',
                'verbose_name': '主页促销活动',
                'db_table': 'df_index_promotion',
            },
        ),
        migrations.AddField(
            model_name='goodsimage',
            name='sku',
            field=models.ForeignKey(to='tt_goods.GoodsSKU', verbose_name='商品SKU'),
        ),
    ]
