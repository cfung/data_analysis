Summary - This is a visulization of baseball data.
The visulization summarizes that lefthanded players, compared to righthanded and both handed players, have hit higher number of home runs, and also have higher batting average

Design - 
v1. initially came up with exploratory charts 
	a. https://gist.github.com/cfung/6ae3adb89bd9c4042088 
	b. https://gist.github.com/cfung/06526540408d06e5605d 
	c. https://gist.github.com/cfung/ff957e0b49bbb341721e 

v2. changed exploratory charts to an explanatory chart after feedback 1a.  

Bar chart was chosen to show the HR difference between right-handed, left-handed and both-handed players because handedness was a categorical variable and bar charts would be good to show the visual differences. 

To show the average of batting average of the players, initially I was thinking to use either line chart or bubble chart.  However with bubble chart, it might not work well along with bar chart, since it can interfere with the bar charts if the circle sizes are too big.  Therefore, I started experiementing with line chart and 2nd axis to highlight the average of batting average 

v3. corrected axis name, added Series to corresponding Y axis for batting average after feedback 1b

v4. after exploring the dataset, many entries of 0 batting average were found.  Final results on the graph did not include these entries.  Please see baseball_data_analysis.py for reference 

v5.  changed labels to Left-Handed, Right-Handed and Both-Handed after feedback 2 and 3

Feedback - 

feedback 1a: Udacity Coach (Carl, 4/7/2016): To me all three look like preliminary exploratory visualizations. Now you need to take the next step and make an explanatory visualization designed from the ground up to tell a particular story or finding. It could be adapted from any of the three you have so far or a new design. 

feedback 1b: Udacity Coach (Carl, 4/12/2016) : Great! Its definitely explanatory now. Udacity Coach: I see a couple issues initially though Udacity Coach: Double axis are tricky, I'm personally not a fan of them at all. But in this case its unclear what is being represented by the bar chart, and what is being represented by the line chart. Udacity Coach: The axis labels are a bit confusing, they should be replace with more accurate and descriptive names. Udacity Coach: Also, is there a reason the points in the line chart line up perfectly with the top of the bars? I'm not sure how to read the visualization.

feedback 2 (from udacity forum):

michael_251502450447

I would add better legend descriptions "L", "R" is not very explanatory

The average line lacks a legend

https://discussions.udacity.com/t/project-6-feedback-baseball-data/162194?u=siu_192607

feedback 3 (from friend Yiu, 4/16/2016)

What do you notice in the visualization?
<Yiu>  Left-Handed baseball players are better in terms of power (HR) and accuracy (batting average)

What questions do you have about the data?
<Yiu>  What year is it?

What relationships do you notice?
<Yiu> You hit harder and more accurate if you're left-handed player

What do you think is the main takeaway from this visualization?
<Yiu> left-handed players are more superior

Is there something you don’t understand in the graphic?
<Yiu>  what is L, R, B?  Why is tooltip show same value but location on the chart is different?




link to my share on forum:  https://discussions.udacity.com/t/project-6-feedback-baseball-data/162194

Resources - http://bl.ocks.org/mbostock/3885304 http://dimplejs.org/examples_index.html http://www.sitepoint.com/create-data-visualizations-javascript-dimple-d3/