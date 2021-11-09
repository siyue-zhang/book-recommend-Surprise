# book-recommend-Surprise

This project is to recommend books to readers based their book ratings from [Book-Crossing Dataset](http://www2.informatik.uni-freiburg.de/~cziegler/BX/), which contains 278,858 users providing 1,149,780 ratings about 271,379 books. To experiment and benchmark different recommendation systems, [Surprise scikit](http://surpriselib.com/) is used, which provides convenient tools to control experiment, handle dataset, adopt cross validation, adopt various ready-to-use prediction algorithms.

## What recommendation system for?

The long-tail problem is common especially in the digital market where the commodity stock is enormous. The graph below shows the distribution of ratings or popularity among items or products in marketplace. While popular items (highly rated by a large number of customers) in blue area consist of a significant part of market value, the unpopular or new items in green area also represent a remarkable share. To satisfy the demand in the long tail, customized recommendation to customers is critical.

<p class="aligncenter">
    <img src="https://miro.medium.com/max/1088/1*9V4i7s4ZxFHMxylZdd6KQg.png" width=400 />
</p>

