<h2><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/">80. Remove Duplicates from Sorted Array II</a></h2><h3>Medium</h3><hr><div element-id="526"><p element-id="525">Given an integer array <code element-id="524">nums</code> sorted in <strong element-id="523">non-decreasing order</strong>, remove some duplicates <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank" element-id="522"><strong element-id="521">in-place</strong></a> such that each unique element appears <strong element-id="520">at most twice</strong>. The <strong element-id="519">relative order</strong> of the elements should be kept the <strong element-id="518">same</strong>.</p>

<p element-id="517">Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the <strong element-id="516">first part</strong> of the array <code element-id="515">nums</code>. More formally, if there are <code element-id="514">k</code> elements after removing the duplicates, then the first <code element-id="513">k</code> elements of <code element-id="512">nums</code>&nbsp;should hold the final result. It does not matter what you leave beyond the first&nbsp;<code element-id="511">k</code>&nbsp;elements.</p>

<p element-id="510">Return <code element-id="509">k</code><em element-id="508"> after placing the final result in the first </em><code element-id="507">k</code><em element-id="506"> slots of </em><code element-id="505">nums</code>.</p>

<p element-id="504">Do <strong element-id="503">not</strong> allocate extra space for another array. You must do this by <strong element-id="502">modifying the input array <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank" element-id="501">in-place</a></strong> with O(1) extra memory.</p>

<p element-id="500"><strong element-id="499">Custom Judge:</strong></p>

<p element-id="498">The judge will test your solution with the following code:</p>

<pre element-id="497">int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i &lt; k; i++) {
    assert nums[i] == expectedNums[i];
}
</pre>

<p element-id="496">If all assertions pass, then your solution will be <strong element-id="495">accepted</strong>.</p>

<p element-id="494">&nbsp;</p>
<p element-id="493"><strong class="example" element-id="492">Example 1:</strong></p>

<pre element-id="491"><strong element-id="490">Input:</strong> nums = [1,1,1,2,2,3]
<strong element-id="489">Output:</strong> 5, nums = [1,1,2,2,3,_]
<strong element-id="488">Explanation:</strong> Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

<p element-id="487"><strong class="example" element-id="486">Example 2:</strong></p>

<pre element-id="485"><strong element-id="484">Input:</strong> nums = [0,0,1,1,1,1,2,3,3]
<strong element-id="483">Output:</strong> 7, nums = [0,0,1,1,2,3,3,_,_]
<strong element-id="482">Explanation:</strong> Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

<p element-id="481">&nbsp;</p>
<p element-id="480"><strong element-id="479">Constraints:</strong></p>

<ul element-id="478">
	<li element-id="477"><code element-id="476">1 &lt;= nums.length &lt;= 3 * 10<sup element-id="475">4</sup></code></li>
	<li element-id="474"><code element-id="473">-10<sup element-id="472">4</sup> &lt;= nums[i] &lt;= 10<sup element-id="471">4</sup></code></li>
	<li element-id="470"><code element-id="469">nums</code> is sorted in <strong element-id="468">non-decreasing</strong> order.</li>
</ul>
</div>