---
title: Struggles and Future
toc: True
description: Chrissie and I decided to create a place to list our troubles coding and how we solved them. We also list our future endeavors in our code.
type: tangibles
courses: { csp: {week: 3}}
---
<!-- Head contains information to Support the Document -->
<head>
    <!-- load jQuery and DataTables output style and scripts -->
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.13.4/css/jquery.dataTables.min.css">
    <script type="text/javascript" language="javascript" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>var define = null;</script>
    <script type="text/javascript" language="javascript" src="https://cdn.datatables.net/1.13.4/js/jquery.dataTables.min.js"></script>

</head>

<!-- Body contains the contents of the Document -->
<body>
    <table id="xdemo" class="table">
        <thead>
            <tr>
                <th>Date</th>
                <th>Who</th>
                <th>Issue</th>
                <th>Solution</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>08/31</td>
                <td>Chrissie</td>
                <td>Linux Shell Edits Are Missing</td>
                <td>Learned that do not make clean and then commit because then all the edits get deleted. Just make.</td>
            </tr>
            <td>08/29</td>
                <td>Arushi</td>
                <td>Quiz Won't Work</td>
                <td>Mr. Mortensen let's me know that quiz.py won't work on HTML code and I can test in my terminal and watch it run there.</td>
                <td>09/06</td>
                <td>Arushi</td>
                <td>Up and Down Arrows on the Game moves the whole game up and down</td>
                <td>Add event default code to keyboard section of the game, so that it won't scroll up and down</td>
            </tr>
        </tbody>
    </table>
</body>

<!-- Script is used to embed executable code -->
<script>
    $("#xdemo").DataTable();
</script>

