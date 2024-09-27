# Weather App

The goal of this problem is to create a frontend Weather application.

You can build your front end on any of these platforms -

- Web
- Mobile App
  - Native iOS
  - Native Android
  - Flutter
  - Any other cross-platform of your choice

You are free to use any frameworks/libraries of your choice for your platform of choice.

Please include documentation (in a file called `SETUP.md`) on any prerequisites we would need to have installed to run your application.

We have provided Figma links that show you mockups and a prototype of what your UI might look like. For web, the mobile designs can be taken as an inspiration. You will receive extra credit for having support for both mobile and tablet/desktop layouts if you chose to implement both.

## Design

Figma prototypes are interactive mockups of apps or websites created in the Figma design tool. They allow you to click through and experience a design just like you would with the real thing, helping you understand how the final product will look and work before it's built.

Prototype Link: [Mobile Prototype](https://www.figma.com/proto/5qCDpXzMfBz0r4NhjR8FbA/Weather-App-(Recruitment)?node-id=135-2492&t=et2vzbxXZPO4z8H2-1&scaling=min-zoom&content-scaling=fixed&page-id=33%3A987&starting-point-node-id=135%3A2492)

## Assets

Assets Link: [Assets](https://www.figma.com/design/5qCDpXzMfBz0r4NhjR8FbA/Weather-App-(Recruitment)?node-id=74-55&t=iNYl4sSV3gNQ3r4d-0)

You will be required to use the assets used for different icons from Figma. To export all the icons together, you can use the shortcut `Command + Shift + E` for Mac OS and `Control + Shift + E` for Windows/Linux.


## Step 1: Build Current Weather UI

Using the [Get Current Weather API](https://raw.githubusercontent.com/Surya-Digital-Interviews/weather-api-public/main/get-climate-details.txt), build the UI that showcases the current weather details. 

[Figma Design Mobile](https://www.figma.com/design/5qCDpXzMfBz0r4NhjR8FbA/Weather-App-(Recruitment)?node-id=126-1307&t=Fsdna9fxBrlTf8ET-4)

## Step 2: Build Forecast UI

Using the [Get Forecast API](https://raw.githubusercontent.com/Surya-Digital-Interviews/weather-api-public/main/get-current-weather.txt), build the UI that showcases the forecast for the next 7 days.

[Figma Design Mobile](https://www.figma.com/design/5qCDpXzMfBz0r4NhjR8FbA/Weather-App-(Recruitment)?node-id=126-1565&t=Fsdna9fxBrlTf8ET-4)

- The 12 hour forecast should support horizontal scrolling to showcase forecast till 12 AM. 
- By default the forecast is shown for the next 7 days.
- Clicking on `15-day weather forecast` should expand the list and show the forecast for the next 15 days. 

## Step 3: Build Additional Weather Details UI

Using the [Get Climate Details API](https://raw.githubusercontent.com/Surya-Digital-Interviews/weather-api-public/main/get-forecast.txt), build the UI that showcases the additional weather details. This includes: 
- Sunrise and Sunset
- Air Quality Index
- Additional Weather Indicators
- Lifestyle Tips

[Figma Design Mobile](https://www.figma.com/design/5qCDpXzMfBz0r4NhjR8FbA/Weather-App-(Recruitment)?node-id=126-2218&t=Fsdna9fxBrlTf8ET-4)
