# **Web-based Visualization Application**

## **Background**

Given a list of over 500 cities randomly drawn from an OpenWeatherMap API, a visualizaton application was created using HTML, CSS, and Javascript. Further, it uses component code block from Bootstrap and Bootswatch. This web application examines the affect that latitude does or does not have on cities located near the equator. Morevever, the applicaton renders graphical depictons of the correlation between latitude vis-a-vis temperature, humidity, cloudiness, and wind velocity.

## Website Link: http://g6-2flyy.github.io/Web-Visualization_Challenge

### This website includes the following seven pages:

* (1) Landing Page
* (4) Visialization Pages
* (1) Comparison Page
* (1) Data Page

### At the top of every page, this website has a navigation bar that does the following:
* Contains the name of the site on the left side of the navigation bar, allowing users to return to the landing page from any page.
* Contains a drop-down menu, named Plots, on the right side of the navigation bar that contains a link to each visualization page.
* Provides two more text links on the right side: Comparisons, which links to the comparisons page, and Data, which links to the data page.
* Is responsive (via media queries). Note that the navigation bar must resemble the one in the screenshots in the Navigation Bar section. In particular, notice the background color change.

## **Landing Page** 

![Reference image](./screenshots/Picture%201.png)

### This page contains the following elements:
1. An explanation of the project.
2. A link to each visualization page. For these, a sidebar should contain a preview image of each visualization. Clicking an image should take the user to that visualization.

## **Visualization Pages**

![Reference image](./screenshots/Picture%202.png)

### Each of the four pages contain the following elements:
1. A descriptive title and a heading tag.
2. The visualization for the selected comparison (latitude vs. max temperature, latitude vs. humidity, latitude vs. cloudiness, or latitude vs. wind speed)
3. A paragraph describing the visualization and its significance.

## **Comparison Page**

![Reference image](./screenshots/Picture%203.png)

### This page does the following:
1. Contains all the visualizations on the same page so that people can easily compare them.
2. Uses a Bootstrap grid for the visualizations. This grid must contain two visualizations across a medium or large screen and one visualization across an extra-small or small screen.

## **Data Page**

![Reference image](./screenshots/Picture%204.png)

### This page displays a responsive table containing data used by the visualizations, as follows:
1. The table must be a Bootstrap table component.
2. The data must come from either exporting or converting the CSV file to HTML. To do so, try using a tool that you already know: Pandas. Pandas has a to_html method that generates an HTML table from a Pandas DataFrame. To learn more, see pandas.DataFrame.to_html Links to an external site.in the official Pandas documentation.

