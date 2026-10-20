{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3ff517d6-57bc-4cc6-b13e-90c4e048b108",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Count of str elements: 3\n"
     ]
    }
   ],
   "source": [
    "my_list = [1, \"apple\", 3.14, True, \"banana\", None, \"cherry\", [1, 2]]\n",
    "\n",
    "string_count = 0\n",
    "\n",
    "for item in my_list:\n",
    "    if type(item) == str:\n",
    "        string_count += 1\n",
    "\n",
    "print(\"Count of str elements:\", string_count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cbf17cde-e3b3-451e-acfb-db56e967bdcf",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
