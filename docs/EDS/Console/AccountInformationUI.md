---
layout: default
title: Account Information
grand_parent: EDS Documentation
parent: Console
nav_order: 2
---

# Table of Contents
* [Introduction](#introduction)
* [General Information](#general-information)
* [My Account](#my-account)
* [My Orders](#my-orders)
* [Order State](#order-state)

## Introduction
The Account Information page is the landing page for each user of the customer account when they login to the [Account Information](https://console.earthdaily.com/account) It allows the user to check his own account details, his orders etc. It also has the link to the other applications like EarthPlatform and EarthMosaics.

## General Information
  
On the upper right hand side of the window, you will see three small icons as below

|   Icon    |   Description     |
|------------|------------------|
| ![About](../assets/AccountUI/About.png) | About page that shows the EarthDaily version |
| ![AppSwitcher](../assets/AccountUI/AppSwitcher.png) | It will show you a list of hosted applications from EarthDaily and you can use it to switch between different applications |
| ![UserInfo](../assets/AccountUI/UserInfo.png) | Quick information about the signed-in user along with his/her account and an option to sign out |

## My Account

| S. No | Label | Description |
|-------|-------|-------------|
| ![One](../assets/NumberLabels/One.png)  | User   |  Logged in user details |
| ![Two](../assets/NumberLabels/Two.png)  | Account | Details of the account that the user belongs to. |
| ![Three](../assets/NumberLabels/Three.png)   | API Credentials |  Token URL to generate “Bearer Token” for API authentication. [Details of How to Provision](../GettingStarted/APIAuthentication.md)  |
| ![Four](../assets/NumberLabels/Four.png)  | Hosted Apps     | Use this to switch between various apps available. |


<br>

Account page for  `New Login experience` 
<br>

![My Account](../assets/AccountUI/AccountInformation.png)

If you are using `Legacy Login`, this is what you would see on your Accounts page

![My Account](../../assets/AccountUI/AccountInformation%20Legacy.png)

## My Orders

It lists all the orders being placed under the customer account you belong to. The purpose of showing all the orders apart from the one you placed is mainly for optimization, to ensure that you don’t end up placing a duplicate order.


| S.No | Label | Description |
|---------|-------|-------------|
| ![Five](../assets/NumberLabels/Five.png)  | My Orders | To go to your orders page. |
| ![Six](../assets/NumberLabels/Six.png)  | Search Filters | You can use the search filters (search by ID, Type, Date range etc) to search for your orders. |
| ![Seven](../assets/NumberLabels/Seven.png) | Order Details Link | This link brings you to a new page that shows all the details related to your order. Once an order is placed, you will see the order in “Processing” state. When the order is completed, it will show “Processed“ and you will also have the Processed date and time for that order. The Product UUID will also show up after the order is processed. This can be helpful to use for searching your product in the destination bucket or troubleshooting.
| ![Eight](../assets/NumberLabels/Eight.png) | Show/Hide Filters | A toggle for you to show/hide the search filters.|
| ![Nine](../assets/NumberLabels/Nine.png) | Show/Hide Columns | Allows you to select the columns you want to view for the search results. |
| ![Ten](../assets/NumberLabels/Ten.png)  | Toggle Density | Allows you to toggle the density of the table. |
| ![Eleven](../assets/NumberLabels/Eleven.png)  | Toggle Full Screen | Allows you to go to full screen mode. |
| ![Twelve](../assets/NumberLabels/Twelve.png) | Refresh | Refreshes the page as per current criteria. |

 
![My Orders](../assets/AccountUI/MyOrders.png)

## Order state

When you place an order, it can go through varous states. Below is a table defining various states and what they mean.

|   Order State         |              Description              |
|-----------------------|-----------------------------------------------------------------------------------------------| 
|   PENDING             |   Order submitted but pending payment and/or approval (eg. mosaic)       |
|   CANCELLED             |   Order cancelled before proceeding (eg. payment failed, etc). Will only be used for orders which could have the “pending” state for now       |
|   IN_PROGRESS             |   Order submitted and under processing       |
|   COMPLETED             |   Order completed with product(s) published to skyfox and ready to use       |
|   PRODUCTION_ERROR             |   Processing failed somewhere along the pipeline, or incase of multiple prodicuts, one or more products were not published successfully to skyfox       |
