# Disk Scheduling Algorithms (Operating System Project)
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>Introduction</h1>
<p>
    Disk scheduling algorithms play a crucial role in optimizing the performance of disk I/O operations by efficiently managing the movement of the disk arm. In this project, we implemented various disk scheduling algorithms and developed a graphical user interface (GUI) for users to visualize and compare these algorithms.
</p>

<h2>Objectives</h2>
<p>The primary objectives of this project were as follows:</p>
<ol>
    <li>Implementation of popular disk scheduling algorithms:
        <ul>
            <li>First-Come, First-Served (FCFS)</li>
            <li>Shortest Seek Time First (SSTF)</li>
            <li>SCAN</li>
            <li>Circular SCAN (C-SCAN)</li>
            <li>LOOK</li>
            <li>Circular LOOK (C-LOOK)</li>
        </ul>
    </li>
    <li>Creation of a user-friendly GUI for interactive visualization of disk scheduling algorithms.</li>
    <li>Comparative analysis of the algorithms based on total head movement and execution time.</li>
</ol>

<h2>Implementation</h2>
<h3>Algorithms Implemented</h3>
<ol>
    <li><b>First-Come, First-Served (FCFS)</b>: Processes requests in the order they arrive.</li>
    <li><b>Shortest Seek Time First (SSTF)</b>: Services the request closest to the current head position first.</li>
    <li><b>SCAN</b>: Moves the disk arm from one end to the other, serving requests along the way, then reverses direction.</li>
    <li><b>Circular SCAN (C-SCAN)</b>: Like SCAN but only moves in one direction, jumping from the last position to the first after reaching the end.</li>
    <li><b>LOOK</b>: Like SCAN but does not travel the full extent of the disk unless necessary.</li>
    <li><b>Circular LOOK (C-LOOK)</b>: Similar to LOOK but only moves in one direction, jumping from the last position to the first after reaching the end.</li>
</ol>

<h3>Graphical User Interface (GUI)</h3>
<p>
    Developed using the customtkinter library for Python, providing a dark-themed, user-friendly interface.
</p>
<ul>
    <li>Allows users to select an algorithm, input request sequence, specify the current position of the disk arm, and set the unit time.</li>
    <li>Provides options to visualize the movement of the disk arm and generate a bar chart comparing total head movement for each algorithm.</li>
</ul>

<h3>Visualization</h3>
<ul>
    <li>Utilized Turtle graphics for real-time visualization of disk arm movement.</li>
    <li>Generated a bar chart using Matplotlib to compare the total head movement of different algorithms.</li>
</ul>

<h2>Results and Analysis</h2>
<ul>
    <li><b>Graphical Visualization:</b> Users can observe the movement of the disk arm in real-time and visualize how each algorithm handles disk requests.</li>
    <li><b>Bar Chart Comparison:</b> A bar chart displays the total head movement for each algorithm, aiding in comparative analysis and algorithm selection based on specific requirements.</li>
</ul>

<h2>Conclusion</h2>
<p>
    In conclusion, our project successfully implemented various disk scheduling algorithms and provided a user-friendly GUI for interactive visualization and analysis. By comparing the performance metrics of different algorithms, users can make informed decisions based on their system requirements and workload characteristics. Future enhancements may include additional scheduling algorithms and advanced visualization techniques for deeper analysis.
</p>

</body>
</html>



