#region License

// 
// Copyright (c) 2011-2012, João Matos Silva <kappy@acydburne.com.pt>
// 
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
// 

#endregion

using System;
using System.Globalization;

namespace DateTimeExtensions.WorkingDays
{
    public static class NigerianPublicHolidays
    {
        /// <summary>
        /// Returns New Year's Day holiday.
        /// </summary>
        public static DateTime NewYearsDay(int year) => new DateTime(year, 1, 1);

        /// <summary>
        /// Returns Workers' Day holiday.
        /// </summary>
        public static DateTime WorkersDay(int year) => new DateTime(year, 5, 1);

        /// <summary>
        /// Returns Democracy Day holiday.
        /// </summary>
        public static DateTime DemocracyDay(int year) => new DateTime(year, 6, 12);

        /// <summary>
        /// Returns Independence Day holiday.
        /// </summary>
        public static DateTime IndependenceDay(int year) => new DateTime(year, 10, 1);

        /// <summary>
        /// Returns Christmas Day holiday.
        /// </summary>
        public static DateTime ChristmasDay(int year) => new DateTime(year, 12, 25);

        /// <summary>
        /// Returns Boxing Day holiday.
        /// </summary>
        public static DateTime BoxingDay(int year) => new DateTime(year, 12, 26);

        /// <summary>
        /// Displays all Nigerian public holidays for a given year.
        /// </summary>
        public static void DisplayHolidays(int year)
        {
            Console.WriteLine("Nigerian Public Holidays for " + year + ":");
            Console.WriteLine($"1. {NewYearsDay(year):D} - New Year's Day");
            Console.WriteLine($"2. {WorkersDay(year):D} - Workers' Day");
            Console.WriteLine($"3. {DemocracyDay(year):D} - Democracy Day");
            Console.WriteLine($"4. {IndependenceDay(year):D} - Independence Day");
            Console.WriteLine($"5. {ChristmasDay(year):D} - Christmas Day");
            Console.WriteLine($"6. {BoxingDay(year):D} - Boxing Day");
        }
    }
}

// Example usage:
// NigerianPublicHolidays.DisplayHolidays(2024);
