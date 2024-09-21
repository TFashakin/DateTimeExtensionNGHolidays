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

using System.Globalization;

namespace DateTimeExtensions.WorkingDays
{
    public static class NigerianPublicHolidays
    {
        private static readonly Calendar NigerianCalendar = new GregorianCalendar(); // Assuming Gregorian calendar is used.

        private static Holiday newYearsDay;
        public static Holiday NewYearsDay
        {
            get
            {
                if (newYearsDay == null)
                {
                    newYearsDay = new FixedHoliday("New Year's Day", new DayInYear(1, 1, NigerianCalendar));
                }
                return newYearsDay;
            }
        }

        private static Holiday workersDay;
        public static Holiday WorkersDay
        {
            get
            {
                if (workersDay == null)
                {
                    workersDay = new FixedHoliday("Workers' Day", new DayInYear(5, 1, NigerianCalendar)); // Corrected to May 1st
                }
                return workersDay;
            }
        }

        private static Holiday democracyDay;
        public static Holiday DemocracyDay
        {
            get
            {
                if (democracyDay == null)
                {
                    democracyDay = new FixedHoliday("Democracy Day", new DayInYear(6, 12, NigerianCalendar));
                }
                return democracyDay;
            }
        }

        private static Holiday independenceDay;
        public static Holiday IndependenceDay
        {
            get
            {
                if (independenceDay == null)
                {
                    independenceDay = new FixedHoliday("Independence Day", new DayInYear(10, 1, NigerianCalendar));
                }
                return independenceDay;
            }
        }

        private static Holiday christmasDay;
        public static Holiday ChristmasDay
        {
            get
            {
                if (christmasDay == null)
                {
                    christmasDay = new FixedHoliday("Christmas Day", new DayInYear(12, 25, NigerianCalendar));
                }
                return christmasDay;
            }
        }

        private static Holiday boxingDay;
        public static Holiday BoxingDay
        {
            get
            {
                if (boxingDay == null)
                {
                    boxingDay = new FixedHoliday("Boxing Day", new DayInYear(12, 26, NigerianCalendar)); // Corrected to Dec 26th
                }
                return boxingDay;
            }
        }
    }
}
