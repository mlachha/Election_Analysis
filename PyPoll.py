{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import the datetime class from the datetime module.\n",
    "import datetime as dt\n",
    "# Use the now() attribute on the datetime class to get the present time.\n",
    "now = dt.datetime.now()\n",
    "# Print the present time.\n",
    "print(\"The time right now is \", now)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Assign a variable for the file to load and the path.\n",
    "#file_to_load = 'Resources/election_results.csv'\n",
    "\n",
    "# Open the election results and read the file.\n",
    "#election_data = open(file_to_load, 'r')\n",
    "\n",
    "#print(type(election_data))\n",
    "# To do: perform analysis.\n",
    "\n",
    "# Close the file.\n",
    "#election_data.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Assign a variable for the file to load and the path.\n",
    "#file_to_load = 'Resources/election_results.csv'\n",
    "\n",
    "#file_to_load = os.path.join(\"Resources\", \"election_results.csv\")\n",
    "\n",
    "# Open the election results and read the file\n",
    "#with open(file_to_load) as election_data:\n",
    "\n",
    "     # To do: perform analysis.\n",
    "    #print(type(election_data))\n",
    "    #print(election_data)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a filename variable to a direct or indirect path to the file.\n",
    "#file_to_save = os.path.join(\"analysis\", \"election_analysis.txt\")\n",
    "# Using the open() function with the \"w\" mode we will write data to the file.\n",
    "#open(file_to_save, \"w\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a filename variable to a direct or indirect path to the file.\n",
    "#file_to_save = os.path.join(\"analysis\", \"election_analysis.txt\")\n",
    "\n",
    "# Using the with statement open the file as a text file.\n",
    "#outfile = open(file_to_save, \"w\")\n",
    "# Write some data to the file.\n",
    "#outfile.write(\"Hello World\")\n",
    "# Close the file\n",
    "#outfile.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a filename variable to a direct or indirect path to the file.\n",
    "#file_to_save = os.path.join(\"analysis\", \"election_analysis.txt\")\n",
    "\n",
    "# Using the with statement open the file as a text file.\n",
    "#with open(file_to_save, \"w\") as txt_file:\n",
    "\n",
    "    # Write some data to the file.\n",
    "    #txt_file.write(\"Hello World\")\n",
    "    #txt_file.write(\"Counties in the Election\\n\")\n",
    "    #txt_file.write(\"--------------------------\\n\")\n",
    "    #txt_file.write(\"Arapahoe\\nDenver\\nJefferson\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Ballot ID', 'County', 'Candidate']\n"
     ]
    }
   ],
   "source": [
    "# Add our dependencies.\n",
    "import csv\n",
    "import os\n",
    "# Assign a variable to load a file from a path.\n",
    "file_to_load = os.path.join(\"Resources\", \"election_results.csv\")\n",
    "# Assign a variable to save the file to a path.\n",
    "file_to_save = os.path.join(\"analysis\", \"election_analysis.txt\")\n",
    "\n",
    "# Open the election results and read the file.\n",
    "with open(file_to_load) as election_data:\n",
    "\n",
    "    # To do: read and analyze the data here.\n",
    "    # Read the file object with the reader function.\n",
    "    file_reader = csv.reader(election_data)\n",
    "    # Print the header row.\n",
    "    headers = next(file_reader)\n",
    "    print(headers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
