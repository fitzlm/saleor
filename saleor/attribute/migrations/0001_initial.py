# Generated by Django 3.1 on 2020-10-30 11:28

import django.db.models.deletion
from django.db import migrations, models

import saleor.core.utils.json_serializer


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("product", "0133_add_attribute_type_and_page_to_attribute_relation"),
        ("page", "0017_pagetype"),
    ]

    state_operations = [
        migrations.CreateModel(
            name="AssignedPageAttribute",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={"db_table": "product_assignedpageattribute"},
        ),
        migrations.CreateModel(
            name="AssignedProductAttribute",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={"db_table": "product_assignedproductattribute"},
        ),
        migrations.CreateModel(
            name="AssignedVariantAttribute",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={"db_table": "product_assignedvariantattribute"},
        ),
        migrations.CreateModel(
            name="Attribute",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "private_metadata",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        encoder=saleor.core.utils.json_serializer.CustomJsonEncoder,
                        null=True,
                    ),
                ),
                (
                    "metadata",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        encoder=saleor.core.utils.json_serializer.CustomJsonEncoder,
                        null=True,
                    ),
                ),
                (
                    "slug",
                    models.SlugField(allow_unicode=True, max_length=250, unique=True),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("product-type", "Product type"),
                            ("page-type", "Page type"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "input_type",
                    models.CharField(
                        choices=[
                            ("dropdown", "Dropdown"),
                            ("multiselect", "Multi Select"),
                        ],
                        default="dropdown",
                        max_length=50,
                    ),
                ),
                ("value_required", models.BooleanField(blank=True, default=False)),
                ("is_variant_only", models.BooleanField(blank=True, default=False)),
                (
                    "visible_in_storefront",
                    models.BooleanField(blank=True, default=True),
                ),
                (
                    "filterable_in_storefront",
                    models.BooleanField(blank=True, default=True),
                ),
                (
                    "filterable_in_dashboard",
                    models.BooleanField(blank=True, default=True),
                ),
                (
                    "storefront_search_position",
                    models.IntegerField(blank=True, default=0),
                ),
                ("available_in_grid", models.BooleanField(blank=True, default=True)),
            ],
            options={
                "db_table": "product_attribute",
                "ordering": ("storefront_search_position", "slug"),
            },
        ),
        migrations.CreateModel(
            name="AttributeValue",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(db_index=True, editable=False, null=True),
                ),
                ("name", models.CharField(max_length=250)),
                ("value", models.CharField(blank=True, default="", max_length=100)),
                ("slug", models.SlugField(allow_unicode=True, max_length=255)),
                (
                    "attribute",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="values",
                        to="attribute.attribute",
                    ),
                ),
            ],
            options={
                "db_table": "product_attributevalue",
                "ordering": ("sort_order", "pk"),
                "unique_together": {("slug", "attribute")},
            },
        ),
        migrations.CreateModel(
            name="AttributeVariant",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(db_index=True, editable=False, null=True),
                ),
                (
                    "assigned_variants",
                    models.ManyToManyField(
                        blank=True,
                        related_name="attributesrelated",
                        through="attribute.AssignedVariantAttribute",
                        to="product.ProductVariant",
                    ),
                ),
                (
                    "attribute",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attributevariant",
                        to="attribute.attribute",
                    ),
                ),
                (
                    "product_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attributevariant",
                        to="product.producttype",
                    ),
                ),
            ],
            options={
                "db_table": "product_attributevariant",
                "ordering": ("sort_order", "pk"),
                "unique_together": {("attribute", "product_type")},
            },
        ),
        migrations.CreateModel(
            name="AttributeProduct",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(db_index=True, editable=False, null=True),
                ),
                (
                    "assigned_products",
                    models.ManyToManyField(
                        blank=True,
                        related_name="attributesrelated",
                        through="attribute.AssignedProductAttribute",
                        to="product.Product",
                    ),
                ),
                (
                    "attribute",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attributeproduct",
                        to="attribute.attribute",
                    ),
                ),
                (
                    "product_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attributeproduct",
                        to="product.producttype",
                    ),
                ),
            ],
            options={
                "db_table": "product_attributeproduct",
                "ordering": ("sort_order", "pk"),
                "unique_together": {("attribute", "product_type")},
            },
        ),
        migrations.CreateModel(
            name="AttributePage",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(db_index=True, editable=False, null=True),
                ),
                (
                    "assigned_pages",
                    models.ManyToManyField(
                        blank=True,
                        related_name="attributesrelated",
                        through="attribute.AssignedPageAttribute",
                        to="page.Page",
                    ),
                ),
                (
                    "attribute",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attributepage",
                        to="attribute.attribute",
                    ),
                ),
                (
                    "page_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attributepage",
                        to="page.pagetype",
                    ),
                ),
            ],
            options={
                "db_table": "product_attributepage",
                "ordering": ("sort_order", "pk"),
                "unique_together": {("attribute", "page_type")},
            },
        ),
        migrations.AddField(
            model_name="attribute",
            name="page_types",
            field=models.ManyToManyField(
                blank=True,
                related_name="page_attributes",
                through="attribute.AttributePage",
                to="page.PageType",
            ),
        ),
        migrations.AddField(
            model_name="attribute",
            name="product_types",
            field=models.ManyToManyField(
                blank=True,
                related_name="product_attributes",
                through="attribute.AttributeProduct",
                to="product.ProductType",
            ),
        ),
        migrations.AddField(
            model_name="attribute",
            name="product_variant_types",
            field=models.ManyToManyField(
                blank=True,
                related_name="variant_attributes",
                through="attribute.AttributeVariant",
                to="product.ProductType",
            ),
        ),
        migrations.AddField(
            model_name="assignedvariantattribute",
            name="assignment",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="variantassignments",
                to="attribute.attributevariant",
            ),
        ),
        migrations.AddField(
            model_name="assignedvariantattribute",
            name="values",
            field=models.ManyToManyField(to="attribute.AttributeValue"),
        ),
        migrations.AddField(
            model_name="assignedvariantattribute",
            name="variant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="attributes",
                to="product.productvariant",
            ),
        ),
        migrations.AddField(
            model_name="assignedproductattribute",
            name="assignment",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="productassignments",
                to="attribute.attributeproduct",
            ),
        ),
        migrations.AddField(
            model_name="assignedproductattribute",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="attributes",
                to="product.product",
            ),
        ),
        migrations.AddField(
            model_name="assignedproductattribute",
            name="values",
            field=models.ManyToManyField(to="attribute.AttributeValue"),
        ),
        migrations.AddField(
            model_name="assignedpageattribute",
            name="assignment",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pageassignments",
                to="attribute.attributepage",
            ),
        ),
        migrations.AddField(
            model_name="assignedpageattribute",
            name="page",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="attributes",
                to="page.page",
            ),
        ),
        migrations.AddField(
            model_name="assignedpageattribute",
            name="values",
            field=models.ManyToManyField(to="attribute.AttributeValue"),
        ),
        migrations.CreateModel(
            name="AttributeValueTranslation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("language_code", models.CharField(max_length=10)),
                ("name", models.CharField(max_length=100)),
                (
                    "attribute_value",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="translations",
                        to="attribute.attributevalue",
                    ),
                ),
            ],
            options={
                "db_table": "product_attributevaluetranslation",
                "unique_together": {("language_code", "attribute_value")},
            },
        ),
        migrations.CreateModel(
            name="AttributeTranslation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("language_code", models.CharField(max_length=10)),
                ("name", models.CharField(max_length=100)),
                (
                    "attribute",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="translations",
                        to="attribute.attribute",
                    ),
                ),
            ],
            options={
                "db_table": "product_attributetranslation",
                "unique_together": {("language_code", "attribute")},
            },
        ),
        migrations.AlterUniqueTogether(
            name="assignedvariantattribute",
            unique_together={("variant", "assignment")},
        ),
        migrations.AlterUniqueTogether(
            name="assignedproductattribute",
            unique_together={("product", "assignment")},
        ),
        migrations.AlterUniqueTogether(
            name="assignedpageattribute", unique_together={("page", "assignment")},
        ),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(state_operations=state_operations)
    ]
